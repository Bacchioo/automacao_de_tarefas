import pyautogui

pyautogui.moveTo(479 ,438 , duration = 1)
distancia = 20089

while distancia > 0 :

    pyautogui.dragRel(distancia, 0, duration = 1)
    distancia = distancia - 10
    pyautogui.dragRel(0, distancia, duration = 1)
    pyautogui.dragRel(-distancia,0, duration = 1)
    distancia = distancia - 10
    pyautogui.dragRel(0,- distancia, duration = 1)

        