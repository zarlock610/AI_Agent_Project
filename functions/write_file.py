import os

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))#This sets a custom path that is the working directory(the floor) and the directory(where we are going to).
    except Exception as e:
        return f"Error: Unable to create absolute path. Line 6. {str(e)}"
    try:
        if os.path.commonpath([full_path, os.path.abspath(working_directory)]) != os.path.abspath(working_directory):#error if full path isn't inside working directory; this is a validator
            raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory. Line 10.')
    except Exception as e:
        return f'Error: Unable to validate path. Line 10. {str(e)}'
    try:
        parent_dir = os.path.dirname(full_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
    except Exception as e:
        return f"Error: Unable to create directories. Line 15. {str(e)}"
    try:
        with open(full_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: Unable to write to file. Line 20. {str(e)}"
    else:
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'