from microbit import *
import utime

uart.init(baudrate=115200)

SOUND_THRESHOLD = 10  # 소리 감지 임계값 설정

keypad = pin1
keypad.set_pull(keypad.PULL_UP)
button_values = {
    'A': (0, 5),
    'B': (65, 75),
    'C': (120, 140),
    'D': (175, 185),
    'E': (640, 645)
}

while True:
    """ Sound """
    sound_level = microphone.sound_level()  # 현재 소리 크기 감지
    if sound_level > SOUND_THRESHOLD:
        uart.write("Sound Detected\n")
        display.show(Image.HEART)
        sound_detected = True  # 감지 상태로 설정하여 반복 전송 방지
        utime.sleep(1)
        display.clear()

    utime.sleep(0.5)  # 상태 체크 간격 설정

    """ Keypad """
    key = keypad.read_analog() # 아날로그 값 읽기

    # 각 버튼의 값을 체크하고 시리얼 통신 전송
    if button_values['A'][0] <= key <= button_values['A'][1]:
        uart.write('W\n')
        # print("W", key)
    elif button_values['B'][0] <= key <= button_values['B'][1]:
        uart.write(' \n')
        # print(" ", key)
    elif button_values['C'][0] <= key <= button_values['C'][1]:
        uart.write('A\n')
        # print("A", key)
    elif button_values['D'][0] <= key <= button_values['D'][1]:
        uart.write('S\n')
        # print("S", key)
    elif button_values['E'][0] <= key <= button_values['E'][1]:
        uart.write('D\n')
        # print("D", key)

    utime.sleep(0.5)  # 주기적으로 확인