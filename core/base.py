import tkinter as tk
from tkinter import ttk
import uuid

class FluentComponent:
    def __init__(self, master=None, id=None, className=None, style=None):
        self.master = master if master else tk.Tk()
        self.id = id if id else str(uuid.uuid4())
        self.className = className
        self.style = style
        self.widget = None

    def create_widget(self):
        raise NotImplementedError("Subclasses must implement create_widget method")

    def pack(self, **kwargs):
        if self.widget:
            self.widget.pack(**kwargs)

    def grid(self, **kwargs):
        if self.widget:
            self.widget.grid(**kwargs)

    def place(self, **kwargs):
        if self.widget:
            self.widget.place(**kwargs)

    def destroy(self):
        if self.widget:
            self.widget.destroy()

    def configure(self, **kwargs):
        if self.widget:
            self.widget.configure(**kwargs)

    def bind(self, sequence=None, func=None, add=None):
        if self.widget:
            self.widget.bind(sequence, func, add)

    def update(self):
        if self.widget:
            self.widget.update()

    def apply_style(self):
        if self.style and self.widget:
            for key, value in self.style.items():
                try:
                    self.widget[key] = value
                except tk.TclError:
                    print(f"警告: 无法设置样式属性 {key}")

    def get_widget(self):
        if not self.widget:
            self.create_widget()
        return self.widget
