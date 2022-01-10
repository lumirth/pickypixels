import PySimpleGUI as sg # for GUI library
import cv2               # for getting video resolution
import shutil            # for moving files
import os                # for deleting files

# v1.0.0

sg.change_look_and_feel('Material2') # Add a touch of color
 
# Left column, to contain list of files to filter
fileColumn = [  [sg.Listbox(values = [], size = (40,15), k = 'LB', horizontal_scroll=True, enable_events=True)],
                [sg.In(visible = False, enable_events=True, k = 'inputFiles')],
                [sg.FilesBrowse('  Add Files  ', target = (-1,0)), sg.Button('  Empty List  ', k = 'emptyList')] ]

# Right column, to contains settings and run button
optionColumn = [ [sg.Text('Specify a resolution to filter out:')],
                 [sg.Spin([i for i in range(0,10000)], initial_value=1920), sg.Text('Width')],
                 [sg.Spin([i for i in range(0,10000)], initial_value=1080), sg.Text('Height')],
                 [sg.Text('Choose a mode:')],
                 [sg.Radio('Delete', "RADIO1", default = False, k = 'delete', enable_events = True),
                  sg.Radio('Output Folder', "RADIO1", default = True, enable_events = True)],
                 [sg.Text('Specify an output folder: ')],
                 [sg.In(size = (30, 6), enable_events=True, k = 'outputFolder')],
                 [sg.FolderBrowse(target=(-1, 0))],
                 [sg.Column([[sg.Button('  RUN  ', k = 'run', enable_events = True)]], justification='r')] ]

# Layout for the entire window
layout = [[sg.Column(fileColumn),sg.Column(optionColumn)]]

# Create the Window
window = sg.Window('pyPickyPixels', layout, resizable=True, element_justification='center')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window
        break
    elif event == 'emptyList': # if user empties list box(list of files)
            window['LB'].update([])
            LB_vals = []
    elif event == 'inputFiles': # if user adds files
            input = values['inputFiles'].split(';') # split the list of inputted files at the semicolon
            newFiles = []
            for i in input: # add filepaths to newFiles list
                newFiles.append(i)
            window.find_element('LB').Update(newFiles) # display listbox values
            LB_vals = newFiles # list for listbox values

    elif event == 'run': # if user hits run button
        listBox = LB_vals
        delete = False # variable for whether delete mode is enable or disable
        worked = False # variable for if operation succeeded or failed
        
        # TODO: add support for ignoring images
        if listBox:
            for file in listBox:
                if values['delete'] == True:
                    delete = True # enables delete mode
                    
                # get video resolution
                vid = cv2.VideoCapture(file)
                width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
                height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
                
                # get target resolution
                targetWidth = values[0]
                targetHeight = values[1]
                
                # operate on files
                try:
                    if width == targetWidth and height == targetHeight:
                        if delete:
                            os.remove(file)
                        else:
                            shutil.move(file, values['outputFolder'])
                    worked = True
                except:
                    sg.Popup('Error Occurred', keep_on_top=True)
            if worked:
                sg.Popup('Operation succeeded', keep_on_top = True)
                        
    # pprint.pprint(values)
window.close()