# automatic-drive
小组成员：刘畅，曹雨辰，毛骏奇，鲁彦锴

参考资料：

[PaddleSeg](https://github.com/PaddlePaddle/PaddleSeg)

[车道线数据集](https://www.kaggle.com/datasets/thomasfermi/lane-detection-for-carla-driving-simulator)

[PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection)

[清华Tinghua100K交通标志数据集.json标签转.xml（python代码）](https://blog.csdn.net/ning_yi/article/details/107541561)

[TT-100k数据集](https://cg.cs.tsinghua.edu.cn/traffic-sign/)

[Micropython API文档](http://docs.micropython.org/en/latest/)

## 一、小车驱动部分

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
