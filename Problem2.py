import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = list()
    all_dir = os.listdir(path);

    for dir in all_dir:
        dir_path = os.path.join(path, dir);
        if os.path.isfile(dir_path) and dir.endswith(suffix):
            result.append(dir_path)
        elif os.path.isdir(dir_path):
            files_in_sub_dir = find_files(suffix, dir_path)
            if files_in_sub_dir != []:
                result.append(files_in_sub_dir)
        
    return result
