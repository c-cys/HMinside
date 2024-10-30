import cv2
import win32gui
import win32con
import serial

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

motion()