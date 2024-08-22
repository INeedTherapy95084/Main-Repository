import pyautogui as gui

ss = gui.screenshot(region=(10, 300, 300, 540))
ss.save(r"D:\E Drive\vscode\Private-Repository\output_image.jpg")