import random
import pyautogui as py
import keyboard as kb

while True:
    if(kb.is_pressed('=')):
        while True:
            x: int = random.randint(100, 1500)
            y: int = random.randint(100, 1000)
            py.moveTo(x,y)
            if(kb.is_pressed('-')):
                break