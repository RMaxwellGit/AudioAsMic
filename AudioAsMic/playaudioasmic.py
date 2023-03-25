import time
import sys
from pygame import mixer

PATH = "C:/Users/rmaxw/OneDrive/Documents/AudioAsMic/AudioAsMic/Sounds/Peter Griffin/"

mixer.init(devicename = 'CABLE Input (VB-Audio Virtual Cable)') # Initialize it with the correct device
mixer.music.load(PATH + sys.argv[1]) # Load the mp3
mixer.music.play() # Play it

while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)