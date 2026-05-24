#python script to keep computer awake, presses F15 key every 3 minutes
#to turn into .exe
#pip install pyinstaller
#pyinstaller --onefile keep_awake.py


import time
import ctypes

# Virtual key code for F15
VK_F15 = 0x7E

KEYEVENTF_KEYUP = 0x0002

def press_f15():
    ctypes.windll.user32.keybd_event(VK_F15, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(VK_F15, 0, KEYEVENTF_KEYUP, 0)


while True:
    press_f15()
    time.sleep(180) #change here (in sec) for longer/shorter duration
