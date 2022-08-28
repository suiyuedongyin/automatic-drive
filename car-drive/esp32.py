# -*-coding:utf-8-*
import socket
from pynput import keyboard

new_socket = socket.socket()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)
port = 52052
print(port)
new_socket.bind((ip, port))
print("init")
new_socket.listen(100)
new_cil, addr = new_socket.accept()
print('新进来的客户端的地址:', addr)

def on_press(key):
    """按下按键时执行。"""
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    if key.char == 'w':
        new_cil.send("forward".encode())
        print("forward")
    elif key.char == 's':
        new_cil.send("back".encode())
        print("back")
    elif key.char == 'k':
        new_cil.send("stop".encode())
        print("stop")
    elif key.char == 'a':
        new_cil.send("left".encode())
        print("left")
    elif key.char == 'j':
        new_cil.send("straight".encode())
    elif key.char == 'd':
        new_cil.send("right".encode())
        print("right")
    elif key.char == '1':
        new_cil.send("sign1".encode())
        print("sign1")
    elif key.char == '2':
        new_cil.send("sign2".encode())
        print("sign2")
    elif key.char == '3':
        new_cil.send("sign3".encode())
        print("sign3")

    # 通过属性判断按键类型。


def on_release(key):
    """松开按键时执行。"""
    # print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
