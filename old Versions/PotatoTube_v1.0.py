import youtube_dl
import tkinter as tk
import re, os

def downloadPath():
    n_cwd=os.getcwd()[:12]
    cwd=n_cwd.replace('\\',"/")
    path=cwd+'Downloads/PotatoTube/'
    return path

def urlTest(data):
    testIs=re.match('https://www.youtube.com/',data)
    return testIs

def getUrlWindow(data=None):
    root=tk.Tk()
    root.withdraw()

    data = root.clipboard_get()

    if urlTest(data) != None:
        print(data, ' is the youtube link and is being downloaded as mp3 file.' )
        return data
    else:
        print('Not a Youtube Link!! Try Again :D ')
        root.clipboard_clear()

    return data

def sendtoYDL(data, path):
    ydl_opts ={
        'outtmpl':path,
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'prefferedcodec': 'mp3',
            'preferredquality': '320',
            }]
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([data])

if __name__ == '__main__':

    data = getUrlWindow()
    sendtoYDL(data, downloadPath())
