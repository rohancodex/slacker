
import pyautogui
from time import sleep

num=1
while(True):
    if(num%2==0):
        pyautogui.moveRel(100, 0, duration = 1)
    else:
        pyautogui.moveRel(-100, 0, duration = 1)
    num+=1
    # Adjust the sleep time as you wish
    sleep(60);