from pathlib import Path
from modules import utils

#import the module
import FreeSimpleGUI as sg

file_path = Path('todo.txt')
file_path.touch(exist_ok = True)

label =  sg.Text("Type in a To-Do")
input_box = sg.Input(tooltip="Enter the Task", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = utils.read_files(file_path), key="todos", enable_events=True, size=[45,10])
edit_button= sg.Button("Edit")


#set the layout
layout =[[label ],[input_box, add_button],[list_box,edit_button]]



window = sg.Window("MY TODO APP ",
                   layout,
                   font=('Helvetica',14))

#this diplays the window on screen
while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
            case "Add":
                todos = utils.read_files(file_path)
                todos.append(values['todo']+ "\n")
                utils.write_to_file(todos,file_path)
                window['todo'].update(value="")
                window['todos'].update(values=todos)


            case "Edit":
                todos_from_file = utils.read_files(file_path)
                todo_to_edit= values['todos'][0]
                index = todos_from_file.index(todo_to_edit)
                new_todo= values['todo'] or todo_to_edit
                todos_from_file[index] = new_todo + "\n"
                utils.write_to_file(todos_from_file, file_path)
                window['todos'].update(values =  todos_from_file)

            case "todos":
                new_value = values["todos"][0]
                window['todo'].update(value = new_value.strip())

            case sg.WINDOW_CLOSED:
                break


window.close()