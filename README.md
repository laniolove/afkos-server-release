- 模拟器设置自定义像素设置：宽720，高1280
    - 进一步减少性能消耗，这边建议模拟器的设置，选择30帧率选项
- 如何运行adb命令，获取serial信息
    - 打开安卓模拟器
    - 打开文件夹中的platform-tools,将adb.exe拖到cmd窗口
    - 输入adb devices,即可获取模拟器的serial信息
    - 随后，打开afk2auto.json文件，设置windowsSerial的值

代码常规书写：
每个界面有应该有特别识别flag，用于定义某个界面特征
if 当前界面标志：
    while 1:
        0.截图
        1.其他界面标记：跳出条件break
        2.当前界面判断：如果是当前界面:
            3.当前界面操作continue