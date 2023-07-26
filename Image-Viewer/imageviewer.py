import PySimpleGUI as sg
import os

first_column = [
    [
        sg.Text("Folder name"),
        sg.In(size=(25,1), enable_events=True, key='abc'),
        sg.FolderBrowse()
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key='abb'
        )
    ]
]

second_column = [
    [sg.T("Choose an image from list on left to display here:")],
    [sg.Text(size=(40, 1), key='tout')],
    [sg.Image(key="-image-")]
]

layout = [
    [
        sg.Column(first_column),
        sg.VSep(),
        sg.Column(second_column)
    ]
]

window = sg.Window("Image viewer", layout)

while True:
    event, value = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "abc":
        folder = value["abc"]
        try:

            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window['abb'].update(fnames)
    elif event == 'abb':
        try:
            filename = os.path.join(
                value['abc'], value['abb'][0]
            )
            window['tout'].update(filename)
            window['-image-'].update(filename = filename)
        except:
            pass

window.close()
