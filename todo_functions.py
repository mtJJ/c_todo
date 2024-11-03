FILEPATH = 'todos.txt'


def get_todos(file_path=FILEPATH):
    with open(file_path, 'r') as file_locaL:
        todos_locaL = file_locaL.readlines()
    return todos_locaL

 
def write_todos(todos_arg, file_path=FILEPATH):
    with open(file_path, 'w') as file:
            file.writelines(todos_arg)