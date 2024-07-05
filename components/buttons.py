import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget

class Button(FluentWidget):
    def __init__(self, master=None, text="", command=None, style="TButton", **kwargs):
        super().__init__(master, **kwargs)
        self.widget = ttk.Button(master, text=text, command=command, style=style)

    def create_widget(self):
        return self.widget

class LinkButton(FluentWidget):
    def __init__(self, master=None, text="", url="", **kwargs):
        super().__init__(master, **kwargs)
        self.url = url
        self.widget = ttk.Label(master, text=text, cursor="hand2", style="Link.TLabel")
        self.widget.bind("<Button-1>", self._open_url)

    def create_widget(self):
        return self.widget

    def _open_url(self, event):
        import webbrowser
        webbrowser.open(self.url)
