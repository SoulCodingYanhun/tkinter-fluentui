# tkinter_fluentui/utils/accessibility.py

import tkinter as tk

class AccessibilityManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AccessibilityManager, cls).__new__(cls)
            cls._instance._last_announcement = None
        return cls._instance

    def announce(self, message):
        """
        向屏幕阅读器发送通知。
        在实际应用中，这个函数应该与操作系统的辅助功能API集成。
        目前，我们只是打印消息作为模拟。

        :param message: 要宣布的消息
        """
        print(f"Screen reader announcement: {message}")
        self._last_announcement = message

    def get_last_announcement(self):
        """
        获取最后一次宣布的消息。用于测试目的。

        :return: 最后一次宣布的消息
        """
        return self._last_announcement

ACCESSIBILITY_MANAGER = AccessibilityManager()

def announce(message):
    """
    向屏幕阅读器发送通知的便捷函数。

    :param message: 要宣布的消息
    """
    ACCESSIBILITY_MANAGER.announce(message)

def set_aria_label(widget, label):
    """
    设置widget的aria-label属性。
    在Tkinter中，我们可以使用`winfo_class()`方法给widget添加自定义属性。

    :param widget: 要设置标签的Tkinter widget
    :param label: aria-label的值
    """
    widget.winfo_class()  # 确保widget已经初始化
    widget.tk.call("wm", "attributes", widget._w, "-aria-label", label)

def get_aria_label(widget):
    """
    获取widget的aria-label属性。

    :param widget: 要获取标签的Tkinter widget
    :return: aria-label的值，如果没有设置则返回None
    """
    widget.winfo_class()  # 确保widget已经初始化
    return widget.tk.call("wm", "attributes", widget._w, "-aria-label")

class KeyboardNavigable:
    """
    可以通过键盘导航的widget的Mixin类。
    """
    def __init__(self):
        self.bind('<Tab>', self._on_tab)
        self.bind('<Shift-Tab>', self._on_shift_tab)

    def _on_tab(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def _on_shift_tab(self, event):
        event.widget.tk_focusPrev().focus()
        return "break"
