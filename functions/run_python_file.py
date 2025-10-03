import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        normalized_path = os.path.normpath(file_path)
        full_path = os.path.realpath(os.path.join(working_directory, normalized_path))#This sets a custom path that is the working directory(the floor) and the directory(where we are going to).
        working_abs = os.path.realpath(working_directory)
        rel_path = os.path.relpath(full_path, working_abs)
        if rel_path.startswith("...") or os.path.isabs(rel_path):
            raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory. Line 6.')
    except Exception as e:
        return f"Error: Unable to create absolute path. Line 6. {str(e)}"
    try:
        if os.path.commonpath([full_path, working_abs]) != working_abs:#error if full path isn't inside working directory; this is a validator
            raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory. Line 10.')
    except Exception as e:
        return f'Error: Unable to validate path. Line 10. {str(e)}'
    try:
        if not os.path.exists(full_path):
            raise Exception(f'Error: File "{file_path}" not found.')
    except Exception as e:
        return f'Error: Unable to verify file existence. Line 15. {str(e)}'
    try:
        if not file_path.endswith(".py"):
            raise Exception(f'Error: File "{file_path}" is not a Python file. Line 20.')
    except Exception as e:
        return f'Error: Unable to validate file type. Line 20. {str(e)}'
    try:
        result = subprocess.run(["python3", full_path] + args, timeout=30, capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        return f"Error: Python script execution failed. Line 27. {e.stderr.decode()}"
    except subprocess.TimeoutExpired as e:
        return f"Error: Python script execution timed out. Line 30. {str(e)}"
    except Exception as e:
        return f"Error: Unable to execute Python script. Line 33. {str(e)}"
    messages = [f"Successfully executed."]

    if result.returncode != 0:
        messages.append(f"Process exited with code {result.returncode}.")
    if not result.stdout.strip() and not result.stderr.strip():
        messages.append("No output produced.")
    else:
        if result.stdout.strip():
            messages.append(f"STDOUT:\n{result.stdout}")
        if result.stderr.strip():
            messages.append(f"STDERR:\n{result.stderr}")
    return "\n".join(messages)
