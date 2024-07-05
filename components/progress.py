from tkinter import ttk
from ..core import FluentWidget

class ProgressBar(FluentWidget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.widget = ttk.Progressbar(master, orient='horizontal', mode='determinate')

    def create_widget(self):
        return self.widget

    def set_progress(self, value):
        self.widget['value'] = value

class Spinner(FluentWidget):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.widget = ttk.Progressbar(master, orient='horizontal', mode='indeterminate')

    def create_widget(self):
        return self.widget

    def start(self):
        self.widget.start()

    def stop(self):
        self.widget.stop()

