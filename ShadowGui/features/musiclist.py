import os
import random

def playmusic():
    music_dir = 'D:\\Audio' # music directry path 
    songs = os.listdir(music_dir)
    rnumber = random.randint(0,len(songs))
    # print(songs)    
    os.startfile(os.path.join(music_dir, songs[rnumber]))