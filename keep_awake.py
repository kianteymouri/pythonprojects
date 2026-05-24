#python script to keep computer awake, moves mouse 1 pixel left and then 1 pixel right every 3 minutes
#to turn into .exe
#pip install pyinstaller
#pyinstaller --onefile keep_awake.py

import time
import pyautogui

INTERVAL_SECONDS = 180

print("Keep Awake is running.")
print("Press Ctrl + C to stop.")

while True:
    pyautogui.moveRel(1, 0)
    time.sleep(0.1)
    pyautogui.moveRel(-1, 0)
    time.sleep(INTERVAL_SECONDS)
