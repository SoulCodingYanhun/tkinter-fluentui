import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget
import os
from ..icon_map import ICON_MAP


class FluentImage(FluentWidget):
    def __init__(self, master=None, source=None, width=None, height=None, **kwargs):
        super().__init__(master, **kwargs)
        self.source = source
        self.width = width
        self.height = height
        self.widget = ttk.Label(master)
        self._load_image()

    def create_widget(self):
        return self.widget

    def _load_image(self):
        if self.source:
            image = tk.PhotoImage(file=self.source)
            if self.width and self.height:
                image = image.subsample(int(image.width() / self.width),
                                        int(image.height() / self.height))
            self.widget.configure(image=image)
            self.widget.image = image  # keep a reference

    def set_image(self, source, width=None, height=None):
        self.source = source
        self.width = width or self.width
        self.height = height or self.height
        self._load_image()


class Icon(FluentWidget):
    FONT_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'FluentSystemIcons-Regular.ttf')

    def __init__(self, master=None, name=None, size=16, color="#000000", **kwargs):
        super().__init__(master, **kwargs)
        self.name = name
        self.size = size
        self.color = color
        self.widget = ttk.Label(master)
        self._load_icon()

    def create_widget(self):
        return self.widget

    def _load_icon(self):
        if self.name in ICON_MAP:
            font = tk.font.Font(family="Fluent System Icons", size=self.size, file=self.FONT_PATH)
            self.widget.configure(text=ICON_MAP[self.name], font=font, foreground=self.color)
        else:
            print(f"Icon '{self.name}' not found.")

    def set_icon(self, name, size=None, color=None):
        self.name = name
        self.size = size or self.size
        self.color = color or self.color
        self._load_icon()

