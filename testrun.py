import sys
import subprocess
from main import solve_error

file_path = "./results/helloworld.py"

def run_file(filename):
    try:
        # Execute the file and capture the output
        result = subprocess.run(['python', filename], capture_output=True, text=True)
        
        # Check if there was an error
        if result.returncode != 0:
            error_message = result.stderr
            return f"Error: {error_message}"
        
        # # If no error, return the output
        # output = result.stdout
        return None
    except Exception as e:
        return f"Error: {str(e)}"

code = ""

with open(file_path, 'r') as file:
    content = file.read()
    code += content

error_log = run_file(file_path)

print(solve_error(code,error_log))


