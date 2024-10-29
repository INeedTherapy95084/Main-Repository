import pyautogui as gui
import time


ss = gui.screenshot(region=(0, 1031, 1900, 50))
ss.save(r"D:\E Drive\vscode\Private-Repository\output_image.jpg")


while True:
   print(gui.position())
   time.sleep(7)