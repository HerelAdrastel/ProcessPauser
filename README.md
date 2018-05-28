I was tired to have my Rainmeter running in background while I’m not watching to it. I decided to create a little script which disables the skins if a window overflows it.

## How to install the script ?
There are few requirements:
- Having a Windows machine
- Having 1 or 2 screens.


You need to install [Python 3](https://www.python.org/downloads/)

Then, to install the dependencies, open Run (Win+R) and enter `pip install pypiwin32`
You need now to download the script on [this](https://github.com/HerelAdrastel/ProcessPauser) repository.
Then, you need to specify the dimensions of your screen. To do that, execute `fullscreen_tester.py`. A command line will appear. Make sure to maximize the window and copy the last value written. (X,X,X,X). If you have a second screen, make the same thing with it.

Now, open `main.py` with notepad and replace the values for `SCREEN1` and `SCREEN2` with the values you obtained with `fullscreen_tester.py`.

Now the script is ready. You can test it by executing the `main.bat` file
If you want to stop the script, go in Run (Win+R) and enter `taskkill /F /IM pythonw.exe`
To make the script start automatically during Windows startup: enter in the run menu and type `shell:startup`. An explorer windows will appear. Copy main.py and main.bat into this explorer window.

I hope my explanations were clear and I hope this script will be useful.
Cheers !
