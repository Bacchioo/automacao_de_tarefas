import pyautogui
import pyscreeze

pyautogui.click(200, 200, interval = .5)
pyautogui.press('space')

while True:
    if pyautogui.pixelMatchesColor(200,430,[83,83,83],70):
        pyautogui.press('space')
    if pyautogui.pixelMatchesColor(200,430,[172,172,172],70):
        pyautogui.press('space')