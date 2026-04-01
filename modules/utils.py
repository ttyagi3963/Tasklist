

def read_files(file_path):
    """
    Write todo to a file
    :return: a list of todos
    """
    with file_path.open('r') as f:
        todos = f.readlines()
    return todos


def write_to_file(todos,file_path):
    """
    Write Todos to files
    :param todos:
    :return: None
    """
    with file_path.open("w") as f:
        f.writelines(todos)



