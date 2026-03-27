from modules import utils

#import the module
import FreeSimpleGUI as sg

#set the layout
layout =[
    [sg.Text("Type in a To-Do")], [sg.Input(tooltip="Enter Todo"), sg.Button('Add')],
]

# sg.theme("")   # Add a touch of color

#create the window

window = sg.Window("MY TODO APP ", layout)

#this diplays the window on screen
window.read()
window.close()