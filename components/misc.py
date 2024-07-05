import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget


class Separator(FluentWidget):
    def __init__(self, master=None, orientation="horizontal", **kwargs):
        super().__init__(master, **kwargs)
        self.widget = ttk.Separator(master, orient=orientation, style="Fluent.TSeparator")

    def create_widget(self):
        return self.widget


class Skeleton(FluentWidget):
    def __init__(self, master=None, width=100, height=20, **kwargs):
        super().__init__(master, **kwargs)
        self.width = width
        self.height = height
        self.widget = tk.Canvas(master, width=width, height=height, bg="#f0f0f0", highlightthickness=0)
        self._animate()

    def create_widget(self):
        return self.widget

    def _animate(self):
        self.widget.delete("all")
        gradient = self.widget.create_rectangle(0, 0, self.width, self.height, fill="#e0e0e0", width=0)
        self.widget.create_rectangle(0, 0, 0, self.height, fill="#f0f0f0", width=0, tags="animation")

        def move_gradient(offset):
            self.widget.coords("animation", offset, 0, offset + self.width // 2, self.height)
            offset += 5
            if offset > self.width:
                offset = -self.width // 2
            self.widget.after(50, move_gradient, offset)

        move_gradient(-self.width // 2)
