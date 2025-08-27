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
            for i in range(0,10):
                gui.leftClick()
            if keyboard.is_pressed('l'):
                break
    if keyboard.is_pressed('`'):
        break
os.system('cls')