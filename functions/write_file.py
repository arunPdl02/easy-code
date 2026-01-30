import os

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        write_file_path = os.path.normpath(os.path.join(working_dir_abs_path, file_path))
        if not os.path.commonpath([working_dir_abs_path, write_file_path]) == working_dir_abs_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(write_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(write_file_path), exist_ok=True)
        with open(write_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as err:
        return f'Error writing file "{file_path}": {err}'

    
    