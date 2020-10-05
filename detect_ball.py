import time
import pyautogui
from playsound import playsound
from PIL import Image
from PIL import ImageChops
import multiprocessing

DELAY=0.1

def play(fname):
    playsound(fname)

if __name__ == '__main__':
    reference = Image.open("images\\ball_reference.png")
    playing_process = None

    while True:
        captured = pyautogui.screenshot(region=(800, 800, 10, 10))
        diff = ImageChops.difference(captured, reference)
        if not diff.getbbox() and playing_process is None:
            print("match!")
            p = multiprocessing.Process(target=play, args=("sounds\deja-vu.mp3",))
            p.start()
            playing_process=p
        else:
            if diff.getbbox() and playing_process:
                playing_process.terminate()
                playing_process = None

        time.sleep(DELAY)
