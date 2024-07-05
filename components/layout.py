from tkinter import ttk
from ..core import FluentWidget

class Stack(FluentWidget):
    def __init__(self, master=None, orientation='horizontal', **kwargs):
        super().__init__(master, **kwargs)
        self.widget = ttk.Frame(master)
        self.orientation = orientation

    def create_widget(self):
        return self.widget

    def add_widget(self, widget, **kwargs):
        if self.orientation == 'horizontal':
            widget.pack(side='left', **kwargs)
        else:
            widget.pack(side='top', **kwargs)
