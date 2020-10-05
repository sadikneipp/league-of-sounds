# league-of-sounds
a way to play sounds based on visual events in LoL

The current implementation just looks at a bunch of reference pixels (`images/ball_reference.png`) inside Nunu's channeling bar. Coordinates for such pixels are hardcoded and likely will need to be adapted to work in other monitors. When a match happens, a process will be spawned playing the audio (`sounds/deja-vu.mp3`) until there is no match.

To run just do `python detect_ball.py` after installing the requirements (`pip install -r requirements.txt`)
