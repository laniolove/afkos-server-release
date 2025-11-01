### pyinstaller打包运行，遇到ppocronnx相关库内容缺失
** 将ppocronnx库，搬到项目目录下，库地址:
```python
import ppocronnx
import os

package_dir = os.path.dirname(ppocronnx.__file__)
print(package_dir)
```
### python模板识别局限性
```
有些图片难以辨别, 建议统一设置模拟器分辨率，然后根据其他模板图片识别，定义相关界面其他元素的位置
```

### windows mumu遇到adb devices无法使用
```
1. 网络打开桥接模式
2. 打开root权限
```

#### 客户端与服务端的问题
```
服务端每条信息最好有独立性
然后客户端自己组合请求信息
服务端定义好数据格式，客户端再接收处理
```

#### 线程
time.sleep(60) 不能暂停子线程，它只会阻塞当前线程。
要暂停 PausableThread 子线程，必须调用 pause() 方法。
PausableThread 的暂停机制是基于 threading.Event 或 threading.Condition 的，确保线程安全。
