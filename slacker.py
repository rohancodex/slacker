import time, pyautogui
import PySimpleGUI as sg
import multiprocessing


def KeepUI():
    
    sg.theme('Dark')
    layout = [
        [sg.Text('Happy Slacking!\nYou can keep this window minimised, and it will continue running.\nClose it to disable it.')]
    ]
    window = sg.Window('Slacker', layout)
    
    p2 = multiprocessing.Process(target = dontsleep)
    p2.start()
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            if p2.is_alive(): 
                p2.terminate()
            break

def dontsleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(300)



if __name__ == '__main__':
    p1 = multiprocessing.Process(target = KeepUI)
    p1.start()
