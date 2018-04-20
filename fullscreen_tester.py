import win32gui
from time import sleep

while True:

    window = win32gui.GetForegroundWindow()
    print(win32gui.GetWindowRect(window))

    sleep(1)