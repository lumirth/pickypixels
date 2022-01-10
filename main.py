import PySimpleGUI as sg

sg.change_look_and_feel('Material2')

# sg.theme('aqua')   # Add a touch of color
# All the stuff inside your window.
fileColumn = [  [sg.Listbox(['fuck','penis','balls'], size = (30,15), k = 'LB')],
                [sg.Button('  Add Files  '), sg.Button('  Empty List  ')] ]

optionColumn = [ [sg.Text('Specify a resolution to filter out:')],
                 [sg.Spin([i for i in range(0,10000)], initial_value=1080), sg.Text('Height')],
                 [sg.Spin([i for i in range(0,10000)], initial_value=1920), sg.Text('Width')],
                 [sg.Text('Choose a mode:')],
                 [sg.Radio('Delete', "RADIO1"),
                  sg.Radio('Output Folder', "RADIO1", default=True)],
                 [sg.T('Specify Output Folder')],
                 [sg.In(size = (30, 6))],
                 [sg.FolderBrowse(target=(-1, 0))],
                 [sg.Column([[sg.Button('  RUN  ')]], justification='r')] ]

"""
event, values = sg.Window('Window Title').Layout([[sg.Input(key='_FILES_'), sg.FilesBrowse()], [sg.OK(), sg.Cancel()]]).Read()

print(values['_FILES_'].split(';'))
"""

layout = [[sg.Column(fileColumn),sg.Column(optionColumn)]]

# Create the Window
window = sg.Window('pyPickyPixels', layout, ttk_theme='default', resizable=True, element_justification='center')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == '  Add Files  ':
            window['LB'].update([])
    if event == '  Empty List  ':
            window['LB'].update([])
    print('You entered ', values[0])

window.close()