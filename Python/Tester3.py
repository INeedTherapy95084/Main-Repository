import pyautogui as gui
import time


ss = gui.screenshot(region=(10, 300, 300, 540))
ss.save(r"D:\E Drive\vscode\Private-Repository\output_image.jpg")


while True:
   print(gui.position())
   time.sleep(7)