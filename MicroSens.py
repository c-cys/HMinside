from microbit import *
import utime
import music

uart.init(baudrate=115200)

PIR = pin5

while True:
    """ MicroCom에게 통신 주는 코드 추가 필요"""

    """ Motion """
    # PIR 센서가 인체를 감지하면 P1의 값이 1로 설정됨
    if PIR.read_digital() == 1:
        uart.write("Motion Detected\n")  # 감지되면 메시지 전송
        display.show(Image.HAPPY)
        set_volume(0)
        music.play(music.BA_DING)
        utime.sleep(1)
        display.clear()