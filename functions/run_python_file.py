import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_path,file_path))
        if os.path.commonpath([abs_path,target_path]) != abs_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if file_path.split(".")[-1] != "py":
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_path]
        if args:
            command.extend(args)
        
        proc = subprocess.run(command, cwd=working_directory,capture_output=True, text=True,timeout=30)

        output = ""
        if proc.returncode != 0:
            output += f"Process exited with code {proc.returncode}\n"

        if not proc.stdout and not proc.stderr :
            output += "No output produced"
        else:
            if proc.stdout:
                output += f"STDOUT: {proc.stdout}"
            if proc.stderr:
                output += f"STDERR: {proc.stderr}"

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"
