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
def sign1():
    ledg.value(0)
    time.sleep(1)
    ledg.value(1)
def sign2():
    ledr.value(0)
    time.sleep(1)
    ledr.value(1)
def sign3():
    ledg.value(0)
    ledr.value(0)
    time.sleep(1)
    ledg.value(1)
    ledr.value(1)



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
    elif order == "sign1":
        sign1()
    elif order == "sign2":
        sign2()
    elif order == "sign3":
        sign3()

    