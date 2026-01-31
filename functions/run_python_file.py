import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if not os.path.commonpath([working_dir_abs, abs_file_path]) == working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if abs_file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python3", abs_file_path]
        if args:
            command.extend(args)
        process = subprocess.run(
            command,
            cwd = working_dir_abs,
            capture_output = True,
            text = True,
            timeout = 30
            )


        result = ""
        if process.returncode != 0:
            result += f"Process exited with code {process.returncode}"
        if not process.stdout and not process.stderr:
            result += "No output produced"
        if process.stdout:
            result += f"\nSTDOUT:\n{process.stdout}"
        if process.stderr:
            result += f"\nSTDERR:\n{process.stderr}"
        return result
    except Exception as err:
        return f"Error: executing Python file: {err}"
