import os
import json
import graphviz

PROJECT_DIR = r"C:\Users\abhiksen\Documents\Hackathon\RepoMind"

EXCLUDED_ENTITIES = {"global", "error_category", "atomic_flag", "exception", "ios_base", "type_info", "locale"}

def generate_design_diagram(parsed_ast_file, output_file, output_format="svg"):
    with open(parsed_ast_file, "r", encoding="utf-8") as f:
        ast_data = json.load(f)
    
    dot = graphviz.Digraph(format=output_format, engine="dot")
    if output_format == "png":
        dot.attr(dpi="300")

    user_classes = {}  # {class_name: base_class}
    function_map = {}  # {class_name: set(function_names)}

    # Extract user-defined classes and their base classes
    for file, data in ast_data.items():
        for class_entry in data.get("classes", []):
            if isinstance(class_entry, dict):
                class_name = class_entry.get("name")
                base_class = class_entry.get("base")  # Base class if available
                
                if class_name and class_name not in EXCLUDED_ENTITIES:
                    user_classes[class_name] = base_class  # Store base relationship
                    dot.node(class_name, shape="box", style="filled", fillcolor="lightblue")
                    function_map[class_name] = set()  # Initialize function storage for class

    # Add inheritance relationships
    for class_name, base_class in user_classes.items():
        if base_class and base_class in user_classes:
            dot.edge(
                base_class,
                class_name,
                label="inherits",
                color="blue",
                fontcolor="blue",
                style="dashed",  # Dashed line for inheritance
                arrowhead="empty",  # Empty arrowhead for clarity
                penwidth="2"  # Slightly thicker for emphasis
            )

    # Extract functions and correctly link them to their parent class
    added_functions = {}  # {"ClassName::FunctionName": {"class": class_name, "function": function_name, "body": None}}
    for file, data in ast_data.items():
        for func_entry in data.get("functions", []):
            if isinstance(func_entry, dict):
                parent_class = func_entry.get("parent")
                func_name = func_entry.get("name")
                return_type = func_entry.get("return_type", "").strip()

                if parent_class in user_classes and func_name:
                    # Ensure function is unique within the same parent class
                    if func_name not in function_map[parent_class]:
                        func_map_entry = f"{func_name} ({return_type})" if return_type else func_name
                        dot.node(func_map_entry, shape="ellipse", style="filled", fillcolor="lightgreen")
                        dot.edge(parent_class, func_map_entry, label="defines")

                        # Mark function as added for this class
                        function_map[parent_class].add(func_name)
                        # Add to function metadata
                        key = f"{class_name}::{func_name}"
                        added_functions[key] = {
                            "class": class_name,
                            "function": func_name,
                            "body": None
                        }

                elif isinstance(func_entry, dict) and func_entry.get("parent") == "global":
                    func_name = func_entry.get("name")
                    body = func_entry.get("body")

                    # Try to match it
                    for key, metadata in added_functions.items():
                        if metadata["function"] == func_name and metadata["body"] is None and body:
                            metadata["body"] = body
                            print(f"🟢 Added body for {key}")
    
    meta_output = os.path.join(PROJECT_DIR, "ast_files", "function_metadata_with_bodies.json")
    with open(meta_output, "w", encoding="utf-8") as f:
        json.dump(added_functions, f, indent=4)

    output_path = os.path.splitext(output_file)[0]
    dot.render(output_path)
    print(f"✅ Design diagram generated: {output_path}.{output_format}")
    print(f"✅ Function metadata saved at: {meta_output}")

parsed_ast_file = os.path.join(PROJECT_DIR, "ast_files", "user_parsed_ast2.json")
output_file = os.path.join(PROJECT_DIR, "design_diagram")
generate_design_diagram(parsed_ast_file, output_file, output_format="svg")
