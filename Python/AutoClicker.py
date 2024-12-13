import os
import time
import pyautogui as gui
import keyboard


os.system('cls')

print("Autoclicker is running...")

stop_region = (0, 1031, 1900, 50)

while True:
    if keyboard.is_pressed('p'):
        while True:
            gui.leftClick()
            if keyboard.is_pressed('l'):
                break
            time.sleep(0.1)
    if keyboard.is_pressed('`'):
        break
os.system('cls')