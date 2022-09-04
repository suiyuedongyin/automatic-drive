# automatic-drive
小组成员：刘畅，曹雨辰，毛骏奇，鲁彦锴

参考资料：

[PaddleSeg](https://github.com/PaddlePaddle/PaddleSeg)

[车道线数据集](https://www.kaggle.com/datasets/thomasfermi/lane-detection-for-carla-driving-simulator)

[PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection)

[清华Tinghua100K交通标志数据集.json标签转.xml（python代码）](https://blog.csdn.net/ning_yi/article/details/107541561)

[TT-100k数据集](https://cg.cs.tsinghua.edu.cn/traffic-sign/)

[Micropython API文档](http://docs.micropython.org/en/latest/)

感谢王铭东老师的MicroPython教程：[Python+ESP32 快速上手](https://www.bilibili.com/video/BV1G34y1E7tE)

感谢大佬up的系列视频：[[Esp32-cam][Micropython]教程-4_socket通信](https://www.bilibili.com/video/BV11F411p7BG?spm_id_from=333.337.search-card.all.click&vd_source=66737e91b0eb7b66f76ada0b474cffe8)

## 一、车道线检测

详见：https://aistudio.baidu.com/aistudio/projectdetail/4366572

## 二、交通信号识别

详见：https://aistudio.baidu.com/aistudio/projectdetail/4390678

## 三、小车驱动
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

## 四、ESP32CAM网页视频推流

可使用Arduino提供的ESP32库中所提供的例程CameraWebServer进行视频推流。

需要修改三个位置:

- const ssid：修改为ESP32CAM需要连接到的网络名称
- const password：修改为ESP32CAM需要连接到的网络密码
- 选择ESP32的型号。不通型号的ESP32已经在程序内#define部分给出。此项目使用AI Thinker(安立信)公式生产的开发板，故将#define CAMERA_MODEL_AI_THINKER语句取消注释，注释掉其他的型号的#define语句。

将ESP32CAM连接到电脑串口，即可开始程序的烧录。烧录完毕后，按下RST键重启ESP32CAM,可在串口监视器中查看ESP32的IP地址，通常为：192.168.XXX.XXX，开启81端口。可通过浏览器输入IP地址访问摄像头的设置页面。

完整的摄像头推流地址为：http://192.168.XXX.XXX:81/stream。通过调用Opencv-python包中的cv2.VideoCapture函数，即可实现视频流的捕获。函数写法为cv2.VideoCapture("http://192.168.XXX.XXX:81/stream")。

## 五、Python端预测部署

在PaddlePaddle中预测引擎和训练引擎底层有着不同的优化方法, 预测引擎使用了AnalysisPredictor，专门针对推理进行了优化，是基于[C++预测库](https://www.paddlepaddle.org.cn/documentation/docs/zh/advanced_guide/inference_deployment/inference/native_infer.html)的Python接口，该引擎可以对模型进行多项图优化，减少不必要的内存拷贝。如果用户在部署已训练模型的过程中对性能有较高的要求，我们提供了独立于PaddleDetection的预测脚本，方便用户直接集成部署。


Python端预测部署主要包含两个步骤：
- 导出预测模型
- 基于Python进行预测

### 1. 导出预测模型

PaddleDetection 在训练过程包括网络的前向和优化器相关参数，而在部署过程中，我们只需要前向参数。模型的导出见模型训练的 AI studio 链接部分。


### 2. 基于Python的预测

#### 2.1 通用检测
在 PaddleDetection 目录下终端输入以下命令进行预测：
```bash
python deploy/python/infer.py --model_dir=./model --camera_id 1  --device=GPU 
```


参数说明如下:

| 参数 | 是否必须| 含义                                                                                          |
|-------|-------|---------------------------------------------------------------------------------------------|
| --model_dir | Yes| 上述导出的模型路径                                                                                   |
| --image_file | Option | 需要预测的图片                                                                                     |
| --image_dir  | Option | 要预测的图片文件夹路径                                                                                 |
| --video_file | Option | 需要预测的视频                                                                                     |
| --camera_id | Option | 用来预测的摄像头ID。**此参数传入的函数经过修改，将infer.py中Detector类中的predict_video方法中的cv2.VideoCapture()函数的参数修改为ESP32CAM的推流地址。当参数camera_id不为-1时，即可捕获摄像头推流进行预测。** |
| --device | Option | 运行时的设备，可选择`CPU/GPU/XPU`，默认为`CPU`                                                            |
| --run_mode | Option | 使用GPU时，默认为paddle, 可选（paddle/trt_fp32/trt_fp16/trt_int8）                                     |
| --batch_size | Option | 预测时的batch size，在指定`image_dir`时有效，默认为1                                                       |
| --threshold | Option| 预测得分的阈值，默认为0.5                                                                              |
| --output_dir | Option| 可视化结果保存的根目录，默认为output/                                                                      |
| --run_benchmark | Option| 是否运行benchmark，同时需指定`--image_file`或`--image_dir`，默认为False                                    |
| --enable_mkldnn | Option | CPU预测中是否开启MKLDNN加速，默认为False                                                                 |
| --cpu_threads | Option| 设置cpu线程数，默认为1                                                                               |
| --trt_calib_mode | Option| TensorRT是否使用校准功能，默认为False。使用TensorRT的int8功能时，需设置为True，使用PaddleSlim量化后的模型时需要设置为False         |
| --save_images | Option| 是否保存可视化结果                                                                                   |
| --save_results | Option| 是否在文件夹下将图片的预测结果以JSON的形式保存                                                                   |


说明：

- 参数优先级顺序：`camera_id` > `video_file` > `image_dir` > `image_file`。
- run_mode：paddle代表使用AnalysisPredictor，精度float32来推理，其他参数指用AnalysisPredictor，TensorRT不同精度来推理。
- 如果安装的PaddlePaddle不支持基于TensorRT进行预测，需要自行编译，详细可参考[预测库编译教程](https://paddleinference.paddlepaddle.org.cn/user_guides/source_compile.html)。
- --run_benchmark如果设置为True，则需要安装依赖`pip install pynvml psutil GPUtil`。
- 如果需要使用导出模型在coco数据集上进行评估，请在推理时添加`--save_results`和`--use_coco_category`参数用以保存coco评估所需要的json文件。

