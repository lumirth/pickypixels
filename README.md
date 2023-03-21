# PickyPixels
A GUI built in Python to filter user videos by resolution, either moving them into a specified output folder or deleting them, depending on user preference.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub version](https://badge.fury.io/gh/lukthony%2Fpypickypixels.svg)](https://github.com/lumirth/pickypixels)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

OSes with binaries:

[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)

OSes supported(but untested):

[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)


<p align="center">
<img width="256" alt="Screen Shot 2022-01-09 at 11 49 11 PM" src="https://user-images.githubusercontent.com/65358837/148723146-80e01e97-8bac-425b-9830-3566af3d2915.png">

<img width="400" alt="Screen Shot 2022-01-09 at 11 49 11 PM" src="https://user-images.githubusercontent.com/65358837/150022604-2bfe5f19-61ae-41ec-9516-bfe6d2b6ea79.png">
</p>

## Installation
PPP(pyPickyPixels) can be installed one of two ways:

- If your OS has a supported binary(currently just macOS), you can download it from the [releases page](https://github.com/lukthony/pyPickyPixels/releases/tag/v1.0.0)
- If your OS doesn't have a supported binary, you can download the [source code](https://github.com/lukthony/pyPickyPixels/archive/refs/heads/main.zip) and run `main.py` using [Python 3.10](https://www.python.org/downloads/release/python-3100/). PPP uses the [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) and [OpenCV](https://pypi.org/project/opencv-python/) modules.

## Usage
PPP supports the following video file formats: `['.webm','.mpg','.mp2','.mpeg','.mpe','.mpv','.ogg','.mp4','.m4p','.m4v','.m4v','.avi','.wmv','.mov','.qt','.flv','.swf','.hevc','.heic']`

<img width="501" alt="Screen Shot 2022-01-09 at 11 49 11 PM" src="https://user-images.githubusercontent.com/65358837/148723122-e0c18604-1456-46e6-b867-726930430342.png">

This is PPP's interface. In order to use it, you can select the `Add Files` button, which will bring up your system's file browser. Select any number of video files, and they will appear in the list. Specify a video resolution to get filtered out, and then decide what happens with video that fit that resolution—are they deleted, or moved to an output folder? Once you're ready, hit `RUN`. If the program successfully deleted/moved your files, it'll say `Operation succeeded`.

## Planned Features

- Support for filtering images as an explicit option
- Allow listbox of files to adjust to file name length
- Filter based on other options besides resolution?

## License
[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## Known Issues
 
  - ~~Images are filtered instead of ignored~~ — **Fixed v1.0.1**
  - Files cannot be added in multiple batches
