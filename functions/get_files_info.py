import os


def get_files_info(working_directory, directory="."):
    # Working directory ist set by us. directory is set by ai-agent. 
    # We need to mitigate potential path traversal vulnerabilities first:

    # 1. Get absolute path from relative path
    abs_path = os.path.abspath(working_directory)
    # 2. create target path by combining the absolute path the target directory
    # 2.1. normalise the path to account for '..' in target directory
    target_path = os.path.normpath(os.path.join(abs_path,directory))
    # 3. check if the largest common path of the working directory absolute path and the absolute target path is the absolute woorking directory path.
    # If that is not the case, this indicates a path traversal attempt (i.e. '../' in target directory)
    if os.path.commonpath([abs_path,target_path]) != abs_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_path):
        return f'Error: "{directory}" is not a directory'
    
    result = ''
    for item in os.listdir(target_path):
        item_name = item
        abs_item_path = os.path.join(target_path,item)
        file_size = os.path.getsize(abs_item_path)
        is_dir = os.path.isdir(abs_item_path)
        file_info = f"- {item_name}: file_size={file_size} bytes, is_dir={is_dir}"
        result = "\n".join([result,file_info])

                  
    return result