from tkinter import ttk
from ..core import FluentWidget

class TextInput(FluentWidget):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.widget = ttk.Entry(master)
        self._set_placeholder()

    def create_widget(self):
        return self.widget

    def _set_placeholder(self):
        self.widget.insert(0, self.placeholder)
        self.widget.bind("<FocusIn>", self._clear_placeholder)
        self.widget.bind("<FocusOut>", self._restore_placeholder)

    def _clear_placeholder(self, event):
        if self.widget.get() == self.placeholder:
            self.widget.delete(0, 'end')

    def _restore_placeholder(self, event):
        if not self.widget.get():
            self.widget.insert(0, self.placeholder)

class SearchBox(TextInput):
    def __init__(self, master=None, placeholder="Search...", command=None, **kwargs):
        super().__init__(master, placeholder=placeholder, **kwargs)
        self.command = command
        self.widget.bind("<Return>", self._on_search)

    def _on_search(self, event):
        if self.command:
            self.command(self.widget.get())
