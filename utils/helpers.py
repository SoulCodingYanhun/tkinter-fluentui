# tkinter_fluentui/utils/helpers.py

import uuid
from datetime import datetime
import time

def generate_id():
    """
    生成一个唯一的ID。

    :return: 唯一ID字符串
    """
    return str(uuid.uuid4())

def format_date(date, format='%Y-%m-%d'):
    """
    格式化日期。

    :param date: datetime对象或者包含时间戳的float
    :param format: 日期格式字符串
    :return: 格式化后的日期字符串
    """
    if isinstance(date, float):
        date = datetime.fromtimestamp(date)
    return date.strftime(format)

def debounce(wait):
    """
    装饰器工厂函数，用于创建一个防抖动装饰器。

    :param wait: 等待时间（秒）
    :return: 防抖动装饰器
    """
    def decorator(fn):
        last_called = [0]
        def debounced(*args, **kwargs):
            now = time.time()
            if now - last_called[0] >= wait:
                last_called[0] = now
                return fn(*args, **kwargs)
        return debounced
    return decorator

def clamp(value, min_value, max_value):
    """
    将值限制在指定范围内。

    :param value: 要限制的值
    :param min_value: 最小值
    :param max_value: 最大值
    :return: 限制后的值
    """
    return max(min_value, min(value, max_value))

def lerp(start, end, alpha):
    """
    线性插值函数。

    :param start: 起始值
    :param end: 结束值
    :param alpha: 插值系数 (0.0 到 1.0)
    :return: 插值结果
    """
    return start + (end - start) * alpha

def hex_to_rgb(hex_color):
    """
    将十六进制颜色转换为RGB元组。

    :param hex_color: 十六进制颜色字符串 (例如 "#FF0000")
    :return: RGB元组 (例如 (255, 0, 0))
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """
    将RGB元组转换为十六进制颜色。

    :param rgb: RGB元组 (例如 (255, 0, 0))
    :return: 十六进制颜色字符串 (例如 "#FF0000")
    """
    return '#{:02x}{:02x}{:02x}'.format(*rgb)
