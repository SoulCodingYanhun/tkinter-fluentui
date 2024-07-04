import tkinter as tk
from ..core.base import FluentComponent
from ..core.styles import apply_theme


class Button(FluentComponent):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.text = text
        self.command = command
        self.create_widget()

    def create_widget(self):
        self.widget = tk.Button(self.master, text=self.text, command=self.command)
        apply_theme(self.widget)


class LinkButton(FluentComponent):
    def __init__(self, master=None, text="", url="", **kwargs):
        super().__init__(master, **kwargs)
        self.text = text
        self.url = url
        self.create_widget()

    def create_widget(self):
        self.widget = tk.Label(self.master, text=self.text, cursor="hand2")
        self.widget.bind("<Button-1>", self.open_url)
        apply_theme(self.widget)

    def open_url(self, event):
        import webbrowser
        webbrowser.open_new(self.url)
