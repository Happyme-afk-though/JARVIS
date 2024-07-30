import threading
import cv2
import imutils
import os
import pyautogui as pg
import time



cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)


alarm = False
alarm_mode = False
alarm_counter = 0


def beep_alarm():
    global alarm
    os.startfile('C:\\Users\\u\\Desktop\\and all\\updated jarvis\\u.mp3')
    time.sleep(0.5)
    pg.click(392,290)
    pg.hotkey('q')
    alarm = False


while True:

    
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_bw

        if threshold.sum() > 100:
            alarm_counter += 1
        else:
            if alarm_counter > 0:
                alarm_counter -= 1

        cv2.imshow("oomm", threshold)
    else:
        cv2.imshow("oomm", frame)

    if alarm_counter > 20:
        if not alarm:
            alarm = True
            threading.Thread(target=beep_alarm).start()

   
    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("t"):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    if key_pressed == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

time.sleep(11)
pg.hotkey("alt",'f4')
os.startfile("C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\jarvis.py")

