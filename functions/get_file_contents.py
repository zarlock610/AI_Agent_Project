from config import MAX_FILE_SIZE
import os

def get_file_contents(working_directory, file_path):
    try:
        if os.path.commonpath([working_directory, file_path]) != os.path.abspath(working_directory):
            raise Exception(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    except Exception as e:
        return f"Error: Unable to validate file path within boundaries. Line 4. {str(e)}"
    try:
        if not os.path.isfile(file_path):
            raise Exception(f'Error: File not found or is not a regular file: "{file_path}"')
    except Exception as e:
        return f"Error: Unable to validate file existence. Line 9. {str(e)}"
    try:
        MAX_CHARS = MAX_FILE_SIZE
    except Exception as e:
        return f"Error: Unable to set MAX_CHARS from config. Line 16. {str(e)}"
    try:
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
    except Exception as e:
        return f"Error: Unable to read file. Line 18. {str(e)}"