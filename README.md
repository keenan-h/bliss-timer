# Bliss Timer

Many of the timers I would use while I was working I found were a little too busy for my purposes and used very unpleasant sounds. So I built this command line timer that prompts you to enter how many minutes before the alarm, then plays a simple riff I recorded on my Casio MT-70 as a more light way to remind you of things. 

## Install
Just need pydub:
```
pip3 install pydub
```
and ffmpeg:
```
brew install ffmpeg
```

## Getting Started
Run the script from within the directory.
```
python3 bliss_timer.py
```
When prompted to enter how many minutes before the timer goes off, enter an integer. 

## Add Your Own Sounds
You can easily add your own sounds for the program to trigger.

New sounds will only work if the file has a 44.1k sample rate and a bit depth of 16.

Just add file to `/sounds` and then in `bliss_timer.py` change the line that selects the file to `./sounds/YOUR_FILE.wav`.