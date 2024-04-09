import pyautogui
import pyscreeze

#Funcoes com o mouse

#Mover
# pyautogui.moveTo(500, 500, duration = 0.5)
# pyautogui.moveRel(100, 0, duration = 0.5)
# pyautogui.moveRel(0, 100, duration = 0.5)

#Arastar

#Clicar
# pyautogui.click(57, 17, duration = 0.5, clicks = 2)

#Localizar um item na tela
btn = pyautogui.locateCenterOnScreen("buscar.png")
pyautogui.click(btn, duration = 0.5)