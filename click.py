import pyautogui

while True:
    pyautogui.click()
    loc = pyautogui.locateOnScreen('coin.png')
    if loc == None:
        pyautogui.press('escape')
    else:
        pyautogui.moveTo(loc)
        pyautogui.click()
    pyautogui.PAUSE = 6
