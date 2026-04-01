from pathlib import Path
from modules import utils

#import the module
import FreeSimpleGUI as sg

#set the layout
layout =[
    [
        sg.Text("Type in a To-Do")],
        [
            sg.Input(tooltip="Enter Todo",key="todo"),
            sg.Button('Add')
        ],
]

file_path = Path('todo.txt')
file_path.touch(exist_ok = True)

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

            case sg.WINDOW_CLOSED:
                break


window.close()