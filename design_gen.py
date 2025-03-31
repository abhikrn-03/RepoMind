import os
import json
import graphviz

PROJECT_DIR = r"C:\Users\abhiksen\Documents\Hackathon\RepoMind"

# List of known system-level parents and classes to exclude
EXCLUDED_ENTITIES = {"global", "error_category", "atomic_flag", "exception", "ios_base", "type_info", "locale", "codecvt", "fpos", "initializer_list", "reverse_iterator", "reference_wrapper", "integer_sequence", "ostreambuf_iterator", "istreambuf_iterator", "checked_array_iterator", "unchecked_array_iterator", "exception_ptr", "numeric_limits", "bad_alloc", "bad_cast", "bad_typeid", "bad_function_call", "bad_weak_ptr", "runtime_error", "logic_error", "length_error", "out_of_range", "range_error", "overflow_error", "underflow_error", "ios", "streambuf", "istream", "ostream", "iostream", "stringstream", "istringstream", "ostringstream", "fstream", "ifstream", "ofstream", "wstreambuf", "wistream", "wostream", "wiostream", "wstringstream", "wistringstream", "wostringstream", "wfstream", "wifstream", "wofstream"}

def generate_design_diagram(parsed_ast_file, output_file, output_format="svg"):
    """Generates a design diagram from parsed AST data using Graphviz."""
    with open(parsed_ast_file, "r", encoding="utf-8") as f:
        ast_data = json.load(f)
    
    dot = graphviz.Digraph(format=output_format, engine="dot")

    if output_format == "png":
        dot.attr(dpi="300")

    # Extract user-defined classes
    user_classes = set()
    for file, data in ast_data.items():
        for class_entry in data.get("classes", []):
            class_name = class_entry.get("name") if isinstance(class_entry, dict) else class_entry
            if class_name and class_name not in EXCLUDED_ENTITIES:
                user_classes.add(class_name)
                dot.node(class_name, shape="box", style="filled", fillcolor="lightblue")

    # Add user-defined functions if their parent is in user_classes
    for file, data in ast_data.items():
        for func_entry in data.get("functions", []):
            if isinstance(func_entry, dict) and func_entry.get("parent") in user_classes:
                func_label = f"{func_entry['parent']}::{func_entry['name']}"
                dot.node(func_label, shape="ellipse", style="filled", fillcolor="lightgreen")

        # Add user-defined function calls as edges
        for call_entry in data.get("calls", []):
            if isinstance(call_entry, dict):
                caller = call_entry.get("caller")
                callee = call_entry.get("callee")
                if caller in user_classes and callee:
                    caller_label = f"{caller}::{callee}"
                    if caller_label != callee:  # Avoid self-referencing edges
                        dot.edge(caller_label, callee)

    # Render the diagram
    output_path = os.path.splitext(output_file)[0]
    dot.render(output_path)
    print(f"✅ Design diagram generated: {output_path}.{output_format}")

# Set input AST file and output file
parsed_ast_file = os.path.join(PROJECT_DIR, "ast_files", "user_parsed_ast2.json")
output_file = os.path.join(PROJECT_DIR, "design_diagram")

# Choose output format: "svg", "pdf", or "png"
generate_design_diagram(parsed_ast_file, output_file, output_format="svg")