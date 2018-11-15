import youtube-dl
import win32clipboard as cp
import re

data= None


def startProgram():
    cp.OpenClipboard()
    cp.EmptyClipboard()

def endProgram():
    cp.CloseClipboard()

def urlTest(data):
    return True

if __name__ == '__main__':

    while data = None:
        data=cp.GetClipboardData()

        if urlTest(data) == True:
            endProgram()
        else:
            continue
