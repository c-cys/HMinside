from microbit import *
import utime

uart.init(baudrate=115200)

PIR = pin5

SOUND_THRESHOLD = 50  # 소리 감지 임계값 설정

keypad = pin1
keypad.set_pull(keypad.PULL_UP)
button_list = [0, 110, 200, 275, 755];
plusminus = 10
button_values = {
    'A': (button_list[0] - plusminus, button_list[0] + plusminus),
    'B': (button_list[1] - plusminus, button_list[1] + plusminus),
    'C': (button_list[2] - plusminus, button_list[2] + plusminus),
    'D': (button_list[3] - plusminus, button_list[3] + plusminus),
    'E': (button_list[4] - plusminus, button_list[4] + plusminus),
}

motor = pin16
spinned = 0

while True:
    """ Motion """
    # PIR 센서가 인체를 감지하면 P1의 값이 1로 설정됨
    if PIR.read_digital() == 1:
        uart.write("Motion Detected\n")  # 감지되면 메시지 전송
        display.show(Image.HAPPY)
        utime.sleep(1)
        display.clear()

    """ Sound """
    sound_level = microphone.sound_level()  # 현재 소리 크기 감지
    if sound_level > SOUND_THRESHOLD:
        uart.write("Sound Detected\n")
        display.show(Image.HEART)
        sound_detected = True  # 감지 상태로 설정하여 반복 전송 방지
        utime.sleep(1)

    """ Keypad """
    key = keypad.read_analog()  # 아날로그 값 읽기
    print(key)
    # 각 버튼의 값을 체크하고 시리얼 통신 전송
    if button_values['A'][0] <= key <= button_values['A'][1]:
        uart.write('W\n')
        # print("W", key)
    elif button_values['B'][0] <= key <= button_values['B'][1]:
        spinned = 1 - spinned
        utime.sleep(1)
        motor.write_digital(spinned)
        motor.write_analog(800 * spinned)
        display.clear()
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