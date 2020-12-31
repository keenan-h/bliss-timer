# need to have ffmpeg installed
# only works with files that are exported at a 44.1k sample rate & a bit depth of 16
# build v1, next looking to make timer that includes seconds.

import time
from pydub import AudioSegment
from pydub.playback import play

minutes = int(input("\nHow many minutes?\n"))
print("\n")
while minutes == 0:
    sound = AudioSegment.from_file("./sounds/alarmsound1_44_16_mono.wav", format="wav")
    quieter_sound = sound - 5
    play(quieter_sound)

while minutes > 1:
    print(str(minutes) + " minutes left.\n")
    time.sleep(60)
    minutes -= 1

print(str(minutes) + " minute left.\n")
time.sleep(60)

sound = AudioSegment.from_file("./sounds/alarmsound1_44_16_mono.wav", format="wav")
quieter_sound = sound - 5
play(quieter_sound)
