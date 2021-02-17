#                                              ___           ___
#     _____                      ___          /  /\         /  /\
#    /  /::\                    /  /\        /  /:/_       /  /:/_
#   /  /:/\:\    ___     ___   /  /:/       /  /:/ /\     /  /:/ /\
#  /  /:/~/::\  /__/\   /  /\ /__/::\      /  /:/ /::\   /  /:/ /::\
# /__/:/ /:/\:| \  \:\ /  /:/ \__\/\:\__  /__/:/ /:/\:\ /__/:/ /:/\:\
# \  \:\/:/~/:/  \  \:\  /:/     \  \:\/\ \  \:\/:/~/:/ \  \:\/:/~/:/
#  \  \::/ /:/    \  \:\/:/       \__\::/  \  \::/ /:/   \  \::/ /:/
#   \  \:\/:/      \  \::/        /__/:/    \__\/ /:/     \__\/ /:/
#    \  \::/        \__\/         \__\/       /__/:/        /__/:/
#     \__\/                                   \__\/         \__\/
#
#       a timer with peaceful alarm
#       code and sounds by: Keenan Hurley
#

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
modified__level_sound = sound - 5
play(modified__level_sound)
