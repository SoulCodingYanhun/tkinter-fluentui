import tkinter as tk
from typing import Optional

class AccessibilityManager:
    def __init__(self):
        self._screen_reader_enabled = False
        self._last_announcement = ""

    def enable_screen_reader(self):
        self._screen_reader_enabled = True

    def disable_screen_reader(self):
        self._screen_reader_enabled = False

    def is_screen_reader_enabled(self) -> bool:
        return self._screen_reader_enabled

    def announce(self, message: str):
        if self._screen_reader_enabled:
            self._last_announcement = message
            # 在实际应用中，这里应该调用操作系统的屏幕阅读器 API
            print(f"Screen Reader: {message}")

    def get_last_announcement(self) -> str:
        return self._last_announcement

    def set_aria_label(self, widget: tk.Widget, label: str):
        widget.configure(text=label)  # 使用 text 属性作为 aria-label 的替代
        widget.configure(takefocus=1)  # 确保小部件可以接收焦点

    def set_aria_description(self, widget: tk.Widget, description: str):
        widget.configure(tooltip=description)  # 使用自定义的 tooltip 属性

accessibility_manager = AccessibilityManager()

def announce(message: str):
    accessibility_manager.announce(message)

def set_aria_label(widget: tk.Widget, label: str):
    accessibility_manager.set_aria_label(widget, label)

def set_aria_description(widget: tk.Widget, description: str):
    accessibility_manager.set_aria_description(widget, description)

def enable_screen_reader():
    accessibility_manager.enable_screen_reader()

def disable_screen_reader():
    accessibility_manager.disable_screen_reader()

def is_screen_reader_enabled() -> bool:
    return accessibility_manager.is_screen_reader_enabled()
