## Python

1. Goto [Python Home Page](https://www.python.org/) and download a version higher than 3.5 or go [here](https://www.python.org/downloads/release/python-367/) and get the right file for your OS.
2. In Windows, while installing make sure to select the 'Add python to PATH' option on the startscreen. This is to make python accessible from the command prompt.
3. Test if it works by typing `python` or `python3` on the Command prompt or Terminal.

## Modules

1. Open command prompt or Terminal and run the following commands;

In Windows,
    
```
python -m pip install --upgrade pip

pip install youtube-dl
```
In Linux and MacOs,

```
python3 -m pip install --upgrade pip

pip3 install youtube-dl
```

## FFMPEG
This is the audio converting part.
### In Windows.

1. Download the zip files from [here](https://ffmpeg.zeranoe.com/builds/).
2. Unzip it to folder of choice.
3. Open Command Prompt in that folder itself as admin (NOT Powershell).
4. Run these commands `setx /M PATH "path\to\ffmpeg\bin;%PATH%"`

### For Mac.

Use this [guide](http://www.renevolution.com/ffmpeg/2013/03/16/how-to-install-ffmpeg-on-mac-os-x.html).

### For Linux(Ubuntu-based)
Open Terminal and run these commands
```
sudo add-apt-repository ppa:mc3man/trusty-media 

sudo apt-get update  

sudo apt-get install ffmpeg  

sudo apt-get install frei0r-plugins  
```

Refer to [Deployment Guide]() find details on running the app.
