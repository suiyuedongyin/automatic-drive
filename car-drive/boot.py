import network
import time
from config import *
from machine import Pin, PWM, Timer



def WIFI_Connect(ssid,password):
    print("ssid:",ssid)
    wlan = network.WLAN(network.STA_IF) #STA 模式
    wlan.active(True) #激活接口
    start_time=time.time() # 记录时间做超时判断
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password) # 输入 WIFI 账号密码
        while not wlan.isconnected():
            #超时判断 ,15 秒没连接成功判定为超时
            if time.time()-start_time > 15 :
                print('WIFI Connected Timeout!')
    if wlan.isconnected():
        #串口打印信息
        print('network information:', wlan.ifconfig())

WIFI_Connect(ssid,password)
ledg=Pin(32,Pin.OUT)
ledr=Pin(33,Pin.OUT)
beep = PWM(Pin(25), freq=100, duty=0)
#a低b高后退，a高b低前进,duty即占空比控制速度，取值范围：1-1023
motor_b = PWM(Pin(27), freq=2000, duty=1023)
motor_a = PWM(Pin(26), freq=2000, duty=1023)
servo_b = PWM(Pin(13), freq=50, duty=0)
ledg.value(0)
ledr.value(0)

time.sleep(3)
ledg.value(1)
ledr.value(1)  