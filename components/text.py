import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget

class Label(FluentWidget):
    def __init__(self, master=None, text="", **kwargs):
        super().__init__(master, **kwargs)
        self.widget = ttk.Label(master, text=text, style="Fluent.TLabel")

    def create_widget(self):
        return self.widget

    def set_text(self, text):
        self.widget.config(text=text)

class Text(FluentWidget):
    def __init__(self, master=None, text="", **kwargs):
        super().__init__(master, **kwargs)
        self.widget = tk.Text(master, wrap=tk.WORD, **kwargs)
        self.widget.insert(tk.END, text)

    def create_widget(self):
        return self.widget

    def get_text(self):
        return self.widget.get("1.0", tk.END)

    def set_text(self, text):
        self.widget.delete("1.0", tk.END)
        self.widget.insert(tk.END, text)
