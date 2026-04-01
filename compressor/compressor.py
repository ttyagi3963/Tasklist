import FreeSimpleGUI as sg
import utils
label1 = sg.Text('Select files to compress')
input1 = sg.Input(key="selected_files")
button1 = sg.FilesBrowse('Choose')


label2 = sg.Text('Select Destination Folder')
input2 = sg.Input(key="dest_folder")
button2 = sg.FolderBrowse('Choose')

button3 =sg.Button("Compress")
output_label = sg.Text("",key='result',text_color="black")

layout = [
    [label1],
    [input1, button1],
    [label2],
    [input2, button2],
    [button3, output_label]
]

window = sg.Window("Compressor", layout)
while True:
    event, values  = window.read()
    print(event)
    print(values)
    filepaths=values["selected_files"]
    filepath_list =  filepaths.split(";")
    folder_path = values['dest_folder']

    was_zipped = utils.make_archive(filepath_list,folder_path)
    if was_zipped:
        window['result'].update(value = "FILES COMPRESSED!" )
    else:
        window['result'].update(value="ERROR!")

