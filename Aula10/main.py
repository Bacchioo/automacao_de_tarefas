import pyautogui

campoAtleta = pyautogui.locateCenterOnScreen("Aula10/Atleta.png", grayscale = True, confidence = 0.8)
print(campoAtleta)