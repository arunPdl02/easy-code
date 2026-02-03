from config import MAX_CHARS
import os
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if not os.path.commonpath([working_dir_abs, abs_file_path]) == working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as err:
        return f'Error reading file "{file_path}"": {err}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content (string) of a specified file inside a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of what file you want the content of, relative to the working directory, just the file name would mean that the file is at the working directory",
            ),
        },
        required=["file_path"],
    ),
)