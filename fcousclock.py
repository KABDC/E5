# 导入time模块，用于获取和处理时间
import time

# 定义一个专注时钟类
class FocusClock:
    # 初始化方法，接受一个专注时间（分钟）作为参数
    def __init__(self, focus_time):
        # 将专注时间转换为秒数，并赋值给self.focus_time
        self.focus_time = focus_time * 60
        # 获取当前时间，并赋值给self.start_time
        self.start_time = time.time()
        # 计算结束时间，并赋值给self.end_time
        self.end_time = self.start_time + self.focus_time
        # 打印开始信息
        print(f"专注时钟开始，你的专注时间是{focus_time}分钟。")
