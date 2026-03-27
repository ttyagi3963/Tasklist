import os
import time
from pathlib import Path;
from modules import utils

now = time.strftime("%c")
print(f"the time is {now}")
file_path = Path('todo.txt')
file_path.touch(exist_ok=True)



while True:
    user_action = input('type ADD or SHOW or EXIT or Edit or mark as COMPLETED: ')
    user_action = user_action.strip().lower()
    try:
        parts = user_action.split(maxsplit=1)
        cmd = parts[0]

        if cmd == 'add' or cmd == 'new':
            todo = parts[1]
            todos = utils.read_files(file_path)
            todos.append(todo + "\n")
            utils.write_to_file(todos, file_path)

        elif (cmd =="show") or (cmd == "display"):
            todos= utils.read_files(file_path)
            print("length =",len(todos))
            if len(todos) == 0:
                print("No Todos have been added")
            else:
                for index, item in enumerate(todos):
                    item = item.strip("\n")
                    row = f"{index + 1}-{item}"
                    print(row)


        elif cmd =='completed':
            try:
                number = int(parts[1])
                todos= utils.read_files(file_path)
                todos.pop(number-1)
                utils.write_to_file(todos, file_path)
            except Exception as e:
                print("invalid index")
                continue

        elif cmd =='edit':
            try:
                number = int(parts[1].strip())
                new_value = input('whats the new value? ')
                todos= utils.read_files(file_path)
                todos[number-1] = new_value + "\n"
                utils.write_to_file(todos, file_path)
            except ValueError:
                print("your command is not valid:")
                continue

        elif cmd =='exit':
            break
        elif cmd == 'delete':
            if(os.path.exists(file_path)):
                os.remove(file_path)
                print(f"{file_path} has been deleted")
            else:
                print(f"file does not exist")
        else:
            print('You entered an unknown command')
    except IndexError as e:
        print(f"command is not valid {e}")
        continue
print('BYE!')









