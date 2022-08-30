import socket
from pynput import keyboard
import cv2
import numpy as np


h1 = 165
h2 = 175
w1 = 175
w2 = 225


cap = cv2.VideoCapture("http://192.168.31.112:81/stream")

while True:
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray_img, 30, 150)
    
    info = canny.shape
    height = info[0]
    width = info[1]

    cnt = 0
    dis = 0

    for i in range(h1, h2):
        for j in range(w1, w2):
            if(canny[i, j] == 255):
                cnt = cnt + 1
    print("cnt: %d" % cnt)


    for i in range(0, height):
        if(canny[width//2, i] == 255):
            print(i)
            dis = i
            break


#dis 表示中轴线上首次检测到白边距底边的距离
#cnt 表示h1h2w1w2围成区域内白色像素点数

    new_cil.send("forward".encode())

    if cnt > 500 or dis < 100:
        new_cil.send("left".encode())
    else:
        new_cil.send("straight".encode())

#画图
    cv2.imshow("Canny", canny)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
