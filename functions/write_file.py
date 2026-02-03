import os
from google.genai import types

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

    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write the given content into the file specifed by the file path which is relative to the working directory",
    parameters= types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path" : types.Schema(
                type=types.Type.STRING,
                description="File path of the file you want to write inside, relative to the working directory, just the file name would mean that the file is at the working directory",
            ),
            "content" : types.Schema(
                type= types.Type.STRING,
                description="what you want to write inside the destination file",
            ),
        },
        required = ["file_path", "content"],
    ),
)
    