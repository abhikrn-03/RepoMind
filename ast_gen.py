import os
import subprocess

def generate_ast_json(src_dir, output_dir):
    """Generates AST JSON files for all .cpp files in the given directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file in os.listdir(src_dir):
        if file.endswith(".cpp"):  # Process only C++ source files
            src_file = os.path.join(src_dir, file)
            ast_file = os.path.join(output_dir, file.replace(".cpp", ".json"))
            
            print(f"Generating AST for {file}...")
            cmd = [
                "clang++", "-Xclang", "-ast-dump=json", "-fsyntax-only", src_file
            ]
            
            try:
                with open(ast_file, "w") as f:
                    subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True, check=True)
                print(f"AST saved: {ast_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing {file}: {e.stderr}")

# Set your project directory
project_dir = r"C:\Users\abhiksen\Documents\Hackathon\RepoMind"
output_dir = os.path.join(project_dir, "ast_files")

# Generate AST JSON files
generate_ast_json(project_dir, output_dir)
