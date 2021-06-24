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
    if suffix is None or not path or not os.path.isdir(path):
        return []

    result = list()
    all_dir = os.listdir(path);

    for dir in all_dir:
        dir_path = os.path.join(path, dir);
        
        if os.path.isfile(dir_path) and dir.endswith(suffix):
            result.append(dir_path)

        elif os.path.isdir(dir_path):
            files_in_sub_dir = find_files(suffix, dir_path)
            if files_in_sub_dir != []:
                result += files_in_sub_dir
        
    return result

def test_case_1():
    """
    Find a list of files that has .c suffix at the testdir
    """
    print("*********Test_case_1***********")
    path = os.path.join(os.path.dirname(__file__), 'testdir')
    result = find_files('.c', path)
    for file in result:
        print(file)

def test_case_2():
    """
    Testing edge case, with suffix is None, should return an empty list
    """
    print("*********Test_case_2***********")
    path = os.path.join(os.path.dirname(__file__), 'testdir')
    result = find_files(None, path)
    print(result)

def test_case_3():
    """
    Testing edge case, with path is None, should return an empty list
    """
    print("*********Test_case_3***********")
    result = find_files('.c', None)
    print(result)

def test_case_4():
    """
    Testing edge case, with suffix is an empty string, should return all files in testdir
    """
    print("*********Test_case_4***********")
    path = os.path.join(os.path.dirname(__file__), 'testdir')
    result = find_files('', path)
    for file in result:
        print(file)

def test_case_5():
    """
    Testing edge case, with path is an empty string, should return an empty list
    """
    print("*********Test_case_5***********")
    result = find_files('.c', "")
    print(result)

def test_case_6():
    """
    Testing edge case, path is not a directory, should return an empty list
    """
    print("*********Test_case_6***********")
    path = os.path.join(os.path.dirname(__file__), 'testdir', 't1.c')
    result = find_files('.c', path)
    print(result)

test_case_1()
test_case_2()
test_case_3()
test_case_4()
test_case_5()
test_case_6()