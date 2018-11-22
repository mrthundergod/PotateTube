import youtube_dl
import tkinter as tk
import re
import msvcrt as ms
data= None


def urlTest(data):
    testIs=re.match('https://www.youtube.com/',data)
    return testIs

def getUrlWindow(data):
    root=tk.Tk()
    show=tk.Label(root, text="Potato Tube")
    show1=tk.Label(root, text="Processing!")
    show.pack()
    show1.pack()
   
    while data == None:
        data = root.clipboard_get()
        #ms.getch()

        if urlTest(data) != None:
            print(data)
            
            return data
        else:
            #data = None
            print('try again')
            continue
    root.mainloop()
    return data

def sendtoYDL(data):
    ydl_opts ={
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'prefferedcodec': 'mp3',
            'preferredquality': '192',
            }]
        }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([data])

if __name__ == '__main__':

    data = getUrlWindow(data)
