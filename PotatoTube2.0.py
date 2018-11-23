import youtube_dl,re, os, tkinter

def getUrlWindow(data=None):
    root=tkinter.Tk()
    root.withdraw()
    data = root.clipboard_get()
    if re.match('https://www.youtube.com/',data) != None:
        print('Downloading as MP3')
        return data
    else: return None

def sendtoYDL(data):
    ydl_opts =  { 'outtmpl':os.getcwd()[:12].replace('\\',"/")+'Downloads/PotatoTube/','format': 'bestaudio/best',
          'postprocessors':[{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'}]}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: ydl.download([data])

if __name__ == '__main__':
    while True:
        data= getUrlWindow()
        if data==None: continue
        sendtoYDL(data)
