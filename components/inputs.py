import tkinter as tk
from ..core.base import FluentComponent
from ..core.styles import apply_theme


class TextInput(FluentComponent):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.create_widget()

    def create_widget(self):
        self.widget = tk.Entry(self.master)
        self.widget.insert(0, self.placeholder)
        self.widget.bind("<FocusIn>", self.clear_placeholder)
        self.widget.bind("<FocusOut>", self.restore_placeholder)
        apply_theme(self.widget)

    def clear_placeholder(self, event):
        if self.widget.get() == self.placeholder:
            self.widget.delete(0, tk.END)

    def restore_placeholder(self, event):
        if not self.widget.get():
            self.widget.insert(0, self.placeholder)


class SearchBox(FluentComponent):
    def __init__(self, master=None, placeholder="Search...", command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.command = command
        self.create_widget()

    def create_widget(self):
        self.frame = tk.Frame(self.master)
        self.entry = tk.Entry(self.frame)
        self.entry.insert(0, self.placeholder)
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.restore_placeholder)
        self.entry.bind("<Return>", self.perform_search)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.search_button = tk.Button(self.frame, text="🔍", command=self.perform_search)
        self.search_button.pack(side=tk.RIGHT)

        self.widget = self.frame
        apply_theme(self.entry)
        apply_theme(self.search_button)

    def clear_placeholder(self, event):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, tk.END)

    def restore_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, self.placeholder)

    def perform_search(self, event=None):
        if self.command:
            self.command(self.entry.get())
