import vlc
import time
import WConio
mode = ""
sound = vlc.MediaPlay("")

def StopPlaying():
    global mode

def playMP3(dir):
    sound = vlc.MediaPlayer("file:///path/to/track.mp3")
    sound.play()
    input("Press enter to stop the sound")

def playYoutube(name):
    pass

def Read():
    music, mode = getData()
    if mode == "mp3":
        playMP3(music)
    elif mode == "youtube":
        playYoutube(music)

def getData():
    pass

if __name__ == "__main__":
    while True:
        while result != "0":
            localtime = time.localtime()
            result = time.strftime("%S", localtime)
            time.sleep(0.1)
        Read()
        
