from functions.config import MAX_FILE_SIZE
import os

def get_file_contents(working_directory, file_path):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))#This sets a custom path that is the working directory(the floor) and the directory(where we are going to).
    except Exception as e:
        return f"Error: Unable to create absolute path. Line 6. {str(e)}"
    try:
        if os.path.commonpath([full_path, os.path.abspath(working_directory)]) != os.path.abspath(working_directory):#error if full path isn't inside working directory; this is a validator
            raise Exception(f'Error: Cannot list "{file_path}" as it is outside the permitted working directory. Line 10.')
    except Exception as e:
        return f'Error: Unable to validate path. Line 10. {str(e)}'
    try:
        if not os.path.isfile(full_path):
            raise Exception(f'Error: File not found or is not a regular file: "{full_path}"')
    except Exception as e:
        return f"Error: Unable to validate file existence. Line 9. {str(e)}"
    try:
        MAX_CHARS = MAX_FILE_SIZE
    except Exception as e:
        return f"Error: Unable to set MAX_CHARS from config. Line 16. {str(e)}"
    try:
        with open(full_path, "r") as f:
            full_content = f.read()
    except Exception as e:
        return f"Error: Unable to read file. Line 18. {str(e)}"
    try:
        if len(full_content) > 10000:
            return full_content[:MAX_CHARS] + f'[...File "{full_path}" truncated at 10000 characters]'
    except Exception as e:
        return f"Error: Unable to give file truncation message. Line 25. {str(e)}"
    return full_content[:MAX_CHARS]
    