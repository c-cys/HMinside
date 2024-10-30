import cv2
import win32gui
import win32con
import serial
import time
import playsound
import pyautogui

# 시리얼 포트 설정
ser = serial.Serial('COM3', 115200)
time.sleep(2)  # 시리얼 통신 안정화 대기
print("Waiting for message...")

window = 1
def motion():
    print("Motion detected by PIR sensor\n-")

    global window
    if window > 1:
        print(window)
        window -= 1
        return
    window += 1

    # 이미지 경로 설정 및 로드
    image_path = r"C:\Users\choiy\Desktop\studying.png"
    image = cv2.imread(image_path)

    # OpenCV 창 설정 및 이미지 표시
    cv2.namedWindow("Studying", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Studying", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Studying", image)

    hwnd = win32gui.FindWindow(None, "Studying")
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def sound():
    # 컴퓨터에 저장되어 있는 녹음된 소리 재생
    print("Playing sound")
    sound_path = r"C:\Users\choiy\Desktop\meow.wav"
    playsound.playsound(sound_path)

def button(data):
    # 키패드 버튼에 따라 W, A, S, D 입력
    if data == "W":
        pyautogui.press('w')
    elif data == "A":
        pyautogui.press('a')
    elif data == "S":
        pyautogui.press('s')
    elif data == "D":
        pyautogui.press('d')

# micro:bit에서 데이터 수신
while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        if data == "Motion Detected":
            motion()
        if data == "Sound Detected":
            sound()
        if data in ("W", " ", "A", "S", "D"):
            button(data)