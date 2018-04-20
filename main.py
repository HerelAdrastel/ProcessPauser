from subprocess import call
from time import sleep

from win32api import EnumDisplayMonitors
from win32gui import EnumWindows, GetWindowRect, GetWindowText, IsWindowVisible
from win32process import GetWindowThreadProcessId

RAINMETER_PATH = "D:\Programs\Rainmeter\Rainmeter.exe"
PROCESS_NAME = "Rainmeter.exe"

SKIN1 = ("Simplon\Clock1", "Simplon\TimeOfDay1", "Herel\CPU1", "Herel\Memory1")
SKIN2 = ("Simplon\Clock2", "Simplon\TimeOfDay2", "Simplon\Visualizer", "Herel\CPU2", "Herel\Memory2")

# Is playing
play_1 = True
play_2 = True

# Before playing
set_to_play_1 = True
set_to_play_2 = True

# Windows in full screen
windows_in_fs_1 = 0
windows_in_fs_2 = 0


def is_in_full_screen_1(_window):
    return GetWindowRect(_window) == (-8, -8, 1374, 746)


# Return true if the window is in full screen and on the second screen
def is_in_full_screen_2(_window):
    return GetWindowRect(_window) == (1358, -8, 2654, 1002)


# Retourne true si blacklisted
def blacklisted(_window):
    return GetWindowText(_window) == "Paramètres" or GetWindowText(_window) == "Photos"


def is_2nd_monitor_connected():
    return len(EnumDisplayMonitors()) >= 2


# noinspection PyUnusedLocal,PyShadowingNames
def on_enumerate(_window, params):
    global windows_in_fs_1
    global windows_in_fs_2

    if is_in_full_screen_1(_window) and not blacklisted(_window):
        windows_in_fs_1 = windows_in_fs_1 + 1
        print("FS 1: {0} {1} Visible: {2}", GetWindowText(_window), GetWindowThreadProcessId(_window)[1], IsWindowVisible(_window))

    if is_in_full_screen_2(_window) and not blacklisted(_window):
        windows_in_fs_2 = windows_in_fs_2 + 1
        #print("FS 2: {0} {1} Visible: {2}", GetWindowText(_window), GetWindowThreadProcessId(_window)[1], IsWindowVisible(_window))


def pause(skin):
    call("{0} !DeactivateConfig {1}".format(RAINMETER_PATH, skin), creationflags=0x00000008)


def play(skin):
    call("{0} !ActivateConfig {1}".format(RAINMETER_PATH, skin), creationflags=0x00000008)


def pause_screen_1():
    print("Pause 1")

    for skin in SKIN1:
        pause(skin)


def play_screen_1():
    print("Play 1")

    for skin in SKIN1:
        play(skin)


def pause_screen_2():
    print("Pause 2")

    for skin in SKIN2:
        pause(skin)


def play_screen_2():
    print("Play 2")

    for skin in SKIN2:
        play(skin)


play_screen_1()
play_screen_2()

while True:

    windows_in_fs_1 = 0
    windows_in_fs_2 = 0

    EnumWindows(on_enumerate, None)

    #print("{0}/{1}".format(windows_in_fs_1, windows_in_fs_2))

    # Test of the first screen
    if windows_in_fs_1 > 0:
        set_to_play_1 = False

    else:
        set_to_play_1 = True

    # Test of the second screen if connected
    if is_2nd_monitor_connected():

        if windows_in_fs_2 > 0:
            set_to_play_2 = False

        else:
            set_to_play_2 = True

    else:
        set_to_play_2 = False

    # Pause screen 2
    if set_to_play_1 is False and play_1 is True:
        pause_screen_1()
        play_1 = False

    # Play screen 2
    if set_to_play_1 is True and play_1 is False:
        play_screen_1()
        play_1 = True

    # Pause screen 2
    if set_to_play_2 is False and play_2 is True:
        pause_screen_2()
        play_2 = False

    # Play screen 2
    if set_to_play_2 is True and play_2 is False:
        play_screen_2()
        play_2 = True

    sleep(1)
