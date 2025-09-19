def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory)#Thiss sets a custom path that is the working directory(the floor) and the directory(where we are going to).
    if not full_path.startswith(os.path.abspath(working_directory)):#error if full path isn't inside working directory; this is a validator
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif: os.path.isdir(directory): #logic for checking if directory is a directory
        if True: return dat_info(full_path) #NOT DONE YET; function dat_info() will go here
        else: raise Exception(f'Error: "{directory}" is not a directory')


def dat_info(file_path):#This is going to comb lists of title, size, and direct true/false in lesson's format.
    title_list = list(os.listdir(file_path))#list of file names only
    file_size_list = []#list of bytes as integers only
    for item in os.listdir(file_path):
        if os.path.isfile(item):
        file_size_list.append(os.path.getsize(item))
    directory_bool_list = list(os.path.isdir(file_path))#list of true/false only
    for name, size, status in zip(title_list, file_size_list, directory_bool_list):#zip() combines separate lists into one list of tuples
        return(f'- {name}: file_size={size} bytes, is_dir={status}')