from tkinter import ttk
from ..core import FluentWidget

class Panel(FluentWidget):
    def __init__(self, master=None, title="", **kwargs):
        super().__init__(master, **kwargs)
        self.widget = ttk.LabelFrame(master, text=title)

    def create_widget(self):
        return self.widget

    def add_widget(self, widget):
        widget.pack(padx=5, pady=5, fill='both', expand=True)
