import pyautogui, time

pyautogui.press('win')
pyautogui.click(780,344, duration = 0.5)
pyautogui.write("calculadora")
pyautogui.click(1000,636, duration = 0.5)

time.sleep(1)

pyautogui.press('2')
pyautogui.press('5')
pyautogui.press('5')

pyautogui.click(72, 86, duration = 0.5)

pyautogui.click(100, 290, duration = 0.5)

pyautogui.click(71, 256, duration = 0.5)
