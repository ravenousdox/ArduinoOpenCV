from PIL import Image
import pyautogui
import random
import time


random.seed(123432)
time.sleep(5)
while True:
    num = random.randrange(100000)
    pyautogui.write("```")
    pyautogui.write("The factors of " + str(num) + " are:")
    pyautogui.hotkey('shift', 'enter')
    for i in range(1, num + 1):
        if num % i == 0:
            pyautogui.write(str(i))
            pyautogui.hotkey('shift', 'enter')
    pyautogui.write("```")
    pyautogui.press('enter')
    time.sleep(0.5 + random.random())
