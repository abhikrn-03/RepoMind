import os
import json
import clang.cindex

PROJECT_DIR = os.path.normpath(r"C:\Users\abhiksen\Documents\Hackathon\RepoMind")
AST_DIR = os.path.join(PROJECT_DIR, "ast_files")
OUTPUT_FILE = os.path.join(AST_DIR, "user_parsed_ast2.json")
SYSTEM_HEADERS = {"iostream", "vector", "string", "map", "set", "bits/stdc++.h"}
SYSTEM_PREFIXES = ("std::", "__", "_", "operator", "builtin", "internal")

def is_system_header(file_path):
    """Checks if the file belongs to a system-defined header."""
    return any(header in file_path for header in SYSTEM_HEADERS)

def is_user_defined(name, file_path, included_from):
    """Returns True if the function/class is user-defined."""
    if not name or name.startswith(SYSTEM_PREFIXES):
        return False
    if included_from:
        included_from = os.path.normpath(included_from)  # Normalize path separators
        if is_system_header(included_from) or not included_from.startswith(PROJECT_DIR):
            return False
    return True

def extract_ast_info(ast_dir, output_file):
    """Extracts user-defined functions, classes, and calls from AST JSON files."""
    extracted_data = {}
    for file in os.listdir(ast_dir):
        if file.endswith(".json"):
            ast_file = os.path.join(ast_dir, file)
            with open(ast_file, "r", encoding="utf-8") as f:
                try:
                    ast_json = json.load(f)
                    extracted_data[file] = parse_ast(ast_json, file)
                except json.JSONDecodeError as e:
                    print(f"Error parsing {file}: {e}")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4)
    print(f"✅ Filtered AST extraction saved to {output_file}")

def extract_function_body(node):
    """ Extract the function body if it contains a CompoundStmt. """
    if "inner" in node:
        for child in node["inner"]:
            if child.get("kind") == "CompoundStmt":
                return json.dumps(child, indent=4)  # Store the entire function body as JSON
    
    return None

def parse_ast(node, filename, parent_name="global", result=None):
    """Recursively parse AST JSON nodes to extract relevant user-defined information."""
    if result is None:
        result = {"functions": [], "classes": [], "calls": []}
    
    if isinstance(node, dict):
        kind = node.get("kind")
        loc = node.get("loc", {})
        file_path = loc.get("file", "")
        included_from = loc.get("includedFrom", {}).get("file", "")
        
        if kind == "CXXRecordDecl":
            class_name = node.get("name")
            tag_used = node.get("tagUsed", "")
            if is_user_defined(class_name, file_path, included_from) and tag_used == "class":
                base_classes = [
                    base["type"]["qualType"]
                    for base in node.get("bases", [])  # Default to empty list if "bases" key is missing
                    if "type" in base and "qualType" in base["type"]
                ]
                seen_classes = {cls["name"] for cls in result["classes"]}
                if class_name not in seen_classes:
                    result["classes"].append({
                        "name": class_name,
                        "file": filename,
                        "base": base_classes[0] if base_classes else None
                    })
                parent_name = class_name
        
        elif kind in ["FunctionDecl", "CXXMethodDecl"]:
            func_name = node.get("name")
            is_builtin = node.get("isImplicit", False)
            return_type = node.get("type", {}).get("qualType", "")
            func_body = extract_function_body(node)
            if is_user_defined(func_name, file_path, included_from) and not is_builtin:
                result["functions"].append({
                    "parent": parent_name,
                    "name": func_name,
                    "return_type": return_type,
                    "file": filename,
                    "body": func_body
                })
        
        elif kind == "CallExpr":
            ref_decl = node.get("referencedDecl", {})
            called_func = ref_decl.get("name", "<unknown>")
            caller_loc = node.get("loc", {})
            caller_file = caller_loc.get("file", "")
            caller_included_from = caller_loc.get("includedFrom", {}).get("file", "")
            if is_user_defined(called_func, caller_file, caller_included_from):
                result["calls"].append({
                    "caller": parent_name,
                    "callee": called_func,
                    "file": filename
                })
        
        for key, value in node.items():
            if key in ["inner", "body", "decls"]:
                parse_ast(value, filename, parent_name, result)
    
    elif isinstance(node, list):
        for item in node:
            parse_ast(item, filename, parent_name, result)
    
    return result

extract_ast_info(AST_DIR, OUTPUT_FILE)
