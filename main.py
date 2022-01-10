import PySimpleGUI as sg # for GUI library
import pprint
"""
import cv2 # for getting video file resolution
file_path = "/Users/lukasunguraitis/Desktop/20220109132357.MP4"  # change to your own video path
vid = cv2.VideoCapture(file_path)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
print(str(int(height))+'x'+str(int(width)))
"""

sg.change_look_and_feel('Material2') # Add a touch of color
 
# Left column, to contain list of files to filter
fileColumn = [  [sg.Listbox([], size = (40,15), k = 'LB', horizontal_scroll=True)],
                [sg.In(visible = False, enable_events=True, k = 'inputFiles')],
                [sg.FilesBrowse('  Add Files  ', target = (-1,0)), sg.Button('  Empty List  ', k = 'emptyList')] ]

# Right column, to contains settings and run button
optionColumn = [ [sg.Text('Specify a resolution to filter out:')],
                 [sg.Spin([i for i in range(0,10000)], initial_value=1080), sg.Text('Height')],
                 [sg.Spin([i for i in range(0,10000)], initial_value=1920), sg.Text('Width')],
                 [sg.Text('Choose a mode:')],
                 [sg.Radio('Delete', "RADIO1", default = False, k = 'delete'),
                  sg.Radio('Output Folder', "RADIO1", default=True)],
                 [sg.T('Specify Output Folder')],
                 [sg.In(size = (30, 6), enable_events=True, k = 'outputFolder')],
                 [sg.FolderBrowse(target=(-1, 0))],
                 [sg.Column([[sg.Button('  RUN  ')]], justification='r')] ]


layout = [[sg.Column(fileColumn),sg.Column(optionColumn)]]

# Create the Window
window = sg.Window('pyPickyPixels', layout, resizable=True, element_justification='center')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window
        break
    elif event == 'emptyList':
            window['LB'].update([])
    elif event == 'inputFiles':
            input = values['inputFiles'].split(';')
            newFiles = []
            for i in input:
                newFiles.append(i)
            window['LB'].update(newFiles)
window.close()