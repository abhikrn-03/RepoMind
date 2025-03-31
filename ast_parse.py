import os
import json

def extract_ast_info(ast_dir, output_file):
    """Extracts function declarations, class declarations, and function calls from AST JSON files."""
    extracted_data = {}
    
    for file in os.listdir(ast_dir):
        if file.endswith(".json"):  # Process only AST JSON files
            ast_file = os.path.join(ast_dir, file)
            
            with open(ast_file, "r", encoding="utf-8") as f:
                try:
                    ast_json = json.load(f)
                    extracted_data[file] = parse_ast(ast_json)
                except json.JSONDecodeError as e:
                    print(f"Error parsing {file}: {e}")
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4)
    
    print(f"AST extraction saved to {output_file}")

def parse_ast(node, parent_name="global", result=None):
    """Recursively parse AST JSON nodes to extract relevant information."""
    if result is None:
        result = {"functions": [], "classes": [], "calls": []}
    
    if isinstance(node, dict):
        kind = node.get("kind")
        
        if kind == "CXXRecordDecl":
            class_name = node.get("name", "<anonymous>")
            if class_name:  # Only add non-empty class names
                result["classes"].append(class_name)
                parent_name = class_name  # Update scope for functions inside classes
        
        elif kind == "FunctionDecl" or kind == "CXXMethodDecl":  # Detect normal and class methods
            func_name = node.get("name", "<anonymous>")
            is_builtin = node.get("isImplicit", False)  # Ignore implicit functions
            
            if not is_builtin and func_name:  # Ensure we capture only user-defined functions
                result["functions"].append((parent_name, func_name))
        
        elif kind == "CallExpr":
            ref_decl = node.get("referencedDecl", {})
            called_func = ref_decl.get("name", "<unknown>")
            if called_func and called_func != "<unknown>":
                result["calls"].append((parent_name, called_func))
        
        # Recursively process children nodes
        for key, value in node.items():
            if key in ["inner", "body", "decls"]:  # Ensure deeper traversal
                parse_ast(value, parent_name, result)
    
    elif isinstance(node, list):
        for item in node:
            parse_ast(item, parent_name, result)
    
    return result

# Set the AST directory and output file
ast_dir = r"C:\Users\abhiksen\Documents\Hackathon\RepoMind\ast_files"
output_file = os.path.join(ast_dir, "parsed_ast.json")

# Extract and save relevant data
extract_ast_info(ast_dir, output_file)
