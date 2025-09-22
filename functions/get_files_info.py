import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, directory))#This sets a custom path that is the working directory(the floor) and the directory(where we are going to).
    except Exception as e:
        return f"Error: Unable to create absolute path. Line 3. {str(e)}"
    try:
        if os.path.commonpath([full_path, os.path.abspath(working_directory)]) != os.path.abspath(working_directory):#error if full path isn't inside working directory; this is a validator
            raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory. Line 7.')
        elif not os.path.isdir(full_path): #logic for checking if directory is a directory
            raise Exception(f"Error: Unable to determine if path is a directory. Line 11.")
        else: return dat_info(full_path) 
    except Exception as e:
        return f'Error: Unable to execute main logic. Line 7. {str(e)}'

#START HERE ADD TRY LOGIC BELOW
def dat_info(file_path):#This is going to comb lists of title, size, and direct true/false in lesson's format.
    try:
        title_list = list(os.listdir(file_path))#list of file names only
    except Exception as e:
        return f"Error: Unable to create title list. Line 18 of dat_info function. {str(e)}"
    try:
        file_size_list = []#list of bytes as integers only
    except Exception as e:
        return f"Error: Unable to create file size list. Line 22 of dat_info function. {str(e)}"
    try:
        for item in os.listdir(file_path):
            full_item_path = os.path.join(file_path, item)
            file_size_list.append(os.path.getsize(full_item_path))
    except Exception as e:
        return f"Error: Unable to populate file size list. Line 26 of dat_info function. {str(e)}"
    try:
        directory_bool_list = [os.path.isdir(os.path.join(file_path, name)) for name in title_list]#list of true/false only
    except Exception as e:
        return f"Error: Unable to create directory boolean list. Line 32 of dat_info function. {str(e)}"
    try:
        results = []
        for name, size, status in zip(title_list, file_size_list, directory_bool_list):#zip() combines separate lists into one list of tuples
            results.append(f'- {name}: file_size={size} bytes, is_dir={status}')
        return "\n".join(results)
    except Exception as e:
        return f"Error: Unable to combine lists. Line 36 of dat_info function. {str(e)}"