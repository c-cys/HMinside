# HMinside
HyeonMin-Inside for physical computing with microbit

## Manual: How to Use
1. Open CMD and run the following command:
```angular2html
git clone https://github.com/c-cys/HMinside
```
```angular2html
pip install opencv-python pywin32 serial playsound pyautogui
```

2. Run [main.py](main.py) on your local editor.\
(ex. IDLE, Mu Editor, VSC, PyCharm)

3. Copy [micro.py](micro.py) and paste on Micro:bit Python Online Editor.\
(https://python.microbit.org/v/3/project)

4. Press the button `Send to micro:bit`.

## Features
1. If the teacher approaches, the [image](src/studying.png) will be opened automatically.
2. If the teacher approaches, motor will be spinned and contribute the tank to go forward. You can defeat your teacher away by physical force.
3. If the teacher call you loud, the [pre-recorded answer](src/answer.mp3) will be played automatically.
4. You can still press W/A/S/D key by pressing keypad buttons.