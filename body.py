import os
import json

PROJECT_DIR = r"C:\Users\abhiksen\Documents\Hackathon\RepoMind"
AST_DIR = os.path.join(PROJECT_DIR, "ast_files")
OUTPUT_FILE = os.path.join(PROJECT_DIR, "function_bodies.json")


def extract_function_bodies(ast_dir, output_file):
    function_data = []

    for ast_file in os.listdir(ast_dir):
        if not ast_file.endswith(".json"):
            continue

        file_path = os.path.join(ast_dir, ast_file)
        with open(file_path, "r", encoding="utf-8") as f:
            ast_json = json.load(f)

        extract_functions(ast_json, function_data)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(function_data, f, indent=4)
    
    print(f"✅ Extracted function bodies saved to {output_file}")


def extract_functions(node, function_data, parent_name=None):
    """ Recursively extract function bodies from AST nodes. """
    if isinstance(node, dict):
        if node.get("kind") in {"FunctionDecl", "CXXMethodDecl"}:
            func_name = node.get("name")
            return_type = node.get("type", {}).get("qualType", "unknown")
            func_body = extract_function_body(node)
            
            if func_body:
                function_data.append({
                    "name": func_name,
                    "parent": parent_name,
                    "return_type": return_type,
                    "body": func_body
                })
        
        # Recurse through children
        for key, value in node.items():
            if key == "inner" and isinstance(value, list):
                for child in value:
                    extract_functions(child, function_data, node.get("name"))

    elif isinstance(node, list):
        for item in node:
            extract_functions(item, function_data, parent_name)


def extract_function_body(node):
    """ Extract the function body if it contains a CompoundStmt. """
    if "inner" in node:
        for child in node["inner"]:
            if child.get("kind") == "CompoundStmt":
                return json.dumps(child, indent=4)  # Store the entire function body as JSON
    
    return None


# Run the function body extraction
extract_function_bodies(AST_DIR, OUTPUT_FILE)
