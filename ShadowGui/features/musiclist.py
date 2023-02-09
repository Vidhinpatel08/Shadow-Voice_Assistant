import os
import random
import subprocess
import features.TTS as TTS

def playmusic(query):
    music_dir = 'D:\\Audio\\music_dir' # music directry path 
    categories = os.listdir(music_dir)
    
    category = None
    for word in query.split(' '):
        if word in [category.lower() for category in categories]:
            category = word
            break

    if category is not None:
        category_dir = os.path.join(music_dir, category)
        category_songs = os.listdir(category_dir)
        rnumber = random.randint(0,len(category_songs))
        stopMusic()
        TTS.speak("Music Starting...")
        os.startfile(os.path.join(category_dir, category_songs[rnumber]))
        return
    
    # If the user's query does not specify a valid category, ask for input
    TTS.speak_Print("\nPlease specify a category (Bhajans, Aartis, Shlokas, Ghazals, Bollywood, General)")
    category = TTS.takeCommand_template()
    if category in [category.lower() for category in categories]:
        category_dir = os.path.join(music_dir, category)
        category_songs = os.listdir(category_dir)
        rnumber = random.randint(0,len(category_songs))
        stopMusic()
        TTS.speak("Music Starting...")
        os.startfile(os.path.join(category_dir, category_songs[rnumber]))
    else:
        TTS.speak_Print("Invalid category")
        playmusic(query)

def stopMusic():
    # check if a process named "wmplayer.exe" is already running and close it
    try:
        process = subprocess.check_output("tasklist", shell=True).decode("utf-8")
        if "wmplayer.exe" in process:
            subprocess.run("taskkill /f /im wmplayer.exe", shell=True, check=True)
    except subprocess.CalledProcessError:
        TTS.speak_Print("Error: unable to close running process")

if __name__ == "__main__":
    playmusic("play music of general")
