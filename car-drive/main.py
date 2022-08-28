from machine import Pin, PWM, Timer
import time
import socket





def Servo(servo,angle):
    servo.duty(int(((angle+90)*2/180+0.5)/20*1023))
def back():
    motor_b.duty(1023)
    motor_a.duty(0)
def forward():
    motor_a.duty(1023)
    motor_b.duty(0)
def stop():
    motor_a.duty(1023)
    motor_b.duty(1023)    
def beepx1():
    beep.freq(200)
    beep.duty(1023)
def beepx2():
    beep.freq(400)
    beep.duty(1023)
def beepx3():
    beep.freq(600)
    beep.duty(1023)
def beepx4():
    beep.freq(800)
    beep.duty(1023)  


addr = ("192.168.31.96",52052)
new_cil = socket.socket()
new_cil.connect(addr)
while 1:
    order=new_cil.recv(1024).decode()
    print(order)
    if order=="forward":
        forward()
    elif order  =="back":
        back()
    elif order == "stop":
        stop()
    elif order == "left":
        Servo(servo_b,-90)
    elif order == "straight":
        Servo(servo_b,0)
    elif order == "right":
        Servo(servo_b,90)
    elif order == "beepx1":
        beepx1()
    elif order == "beepx2":
        beepx2()
    elif order == "beepx3":
        beepx3()
    elif order == "beepx4":
        beepx4()
    