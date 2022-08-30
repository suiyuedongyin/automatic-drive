# automatic-drive
## 一、小车驱动

### 1.环境配置

下载:[ESP32MicroPython固件](https://micropython.org/download/esp32/),[CP210x驱动](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads),[Thonny](https://thonny.org/)

安装：

1. 给电脑安装上CP210x驱动，保证在设备管理器中的端口（COM和LPT）出能查询到COM号
2. 安装Thonny，进入到工具栏-设置-解释器，选择MicroPython(ESP32)解释器，点击右下角的Install or update firmware, Port选择上步中的COM号，Firmware选择下载好的MicroPython固件，并且勾选Erase flash before installing, 点击安装
3. 安装成功后退到主页面，点击红色的STOP图表，在Shell中出现MicroPython并能运行print("Hello, ESP32! ")说明环境配置成功

### 2.上传代码

将car-drive中的main.py和boot.py保存至EPS32中（在连接ESP32后，保存文件会有此电脑和MicroPython两个选项，选择MicroPython即可）

此外新建config.py文件，设置ssid和password:

```python
ssid = "ssid"
password = "password"
```

### 3.运行

电脑端运行esp32.py，接着按下小车端RST按键，等待esp32连接至电脑后，即可用键盘控制小车（键盘中的AWSD分别控制左转，前进，后退，右转，JK分别控制调直，停止，Esc键可退出小车驱动）
