import uuid
import time
from typing import Callable, Any, Optional
import tkinter as tk
from tkinter import font as tkfont

def generate_id() -> str:
    """生成唯一ID"""
    return str(uuid.uuid4())

def format_date(date: Any, format_str: str = '%Y-%m-%d') -> str:
    """格式化日期"""
    return date.strftime(format_str)

def debounce(wait: float) -> Callable:
    """
    装饰器：防抖函数
    :param wait: 等待时间（秒）
    """
    def decorator(fn: Callable) -> Callable:
        last_called = [0.0]
        def debounced(*args: Any, **kwargs: Any) -> Any:
            now = time.time()
            if now - last_called[0] >= wait:
                last_called[0] = now
                return fn(*args, **kwargs)
        return debounced
    return decorator

def throttle(wait: float) -> Callable:
    """
    装饰器：节流函数
    :param wait: 等待时间（秒）
    """
    def decorator(fn: Callable) -> Callable:
        last_called = [0.0]
        def throttled(*args: Any, **kwargs: Any) -> Any:
            now = time.time()
            if now - last_called[0] >= wait:
                last_called[0] = now
                return fn(*args, **kwargs)
        return throttled
    return decorator

def create_font(family: str, size: int, weight: str = 'normal', slant: str = 'roman') -> tkfont.Font:
    """创建字体对象"""
    return tkfont.Font(family=family, size=size, weight=weight, slant=slant)

def get_widget_width(widget: tk.Widget) -> int:
    """获取小部件的宽度"""
    widget.update_idletasks()
    return widget.winfo_width()

def get_widget_height(widget: tk.Widget) -> int:
    """获取小部件的高度"""
    widget.update_idletasks()
    return widget.winfo_height()

def center_window(window: tk.Tk, width: int, height: int):
    """将窗口居中"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

def create_tooltip(widget: tk.Widget, text: str):
    """为小部件创建工具提示"""
    tooltip = tk.Label(widget.master, text=text, background="#ffffe0", relief="solid", borderwidth=1)
    tooltip.place_forget()

    def enter(event):
        tooltip.lift(aboveThis=widget)
        tooltip.place(x=widget.winfo_rootx(), y=widget.winfo_rooty() + widget.winfo_height())

    def leave(event):
        tooltip.place_forget()

    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

def validate_email(email: str) -> bool:
    """简单的电子邮件验证"""
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def limit_text_length(text: str, max_length: int) -> str:
    """限制文本长度，超出部分用省略号替代"""
    return (text[:max_length-3] + '...') if len(text) > max_length else text

def rgb_to_hex(r: int, g: int, b: int) -> str:
    """RGB颜色值转换为十六进制颜色代码"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex_to_rgb(hex_color: str) -> tuple:
    """十六进制颜色代码转换为RGB颜色值"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
