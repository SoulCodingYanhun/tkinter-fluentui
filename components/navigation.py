import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget

class Breadcrumb(FluentWidget):
    def __init__(self, master=None, items=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.items = items or []
        self.command = command
        self.widget = ttk.Frame(master)
        self._create_breadcrumb()

    def create_widget(self):
        return self.widget

    def _create_breadcrumb(self):
        for i, item in enumerate(self.items):
            if i > 0:
                ttk.Label(self.widget, text=">", style="Fluent.TLabel").pack(side=tk.LEFT, padx=(2, 2))
            btn = ttk.Button(self.widget, text=item, style="Fluent.TButton", command=lambda x=i: self._on_click(x))
            btn.pack(side=tk.LEFT)

    def _on_click(self, index):
        if self.command:
            self.command(self.items[index])

class CommandBar(FluentWidget):
    def __init__(self, master=None, commands=None, **kwargs):
        super().__init__(master, **kwargs)
        self.commands = commands or []
        self.widget = ttk.Frame(master)
        self._create_command_bar()

    def create_widget(self):
        return self.widget

    def _create_command_bar(self):
        for cmd in self.commands:
            btn = ttk.Button(self.widget, text=cmd['text'], style="Fluent.TButton", command=cmd['command'])
            btn.pack(side=tk.LEFT, padx=(0, 5))

class NavMenu(FluentWidget):
    def __init__(self, master=None, items=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.items = items or []
        self.command = command
        self.widget = ttk.Frame(master)
        self._create_nav_menu()

    def create_widget(self):
        return self.widget

    def _create_nav_menu(self):
        for item in self.items:
            btn = ttk.Button(self.widget, text=item['text'], style="Fluent.TButton", command=lambda x=item: self._on_click(x))
            btn.pack(anchor=tk.W, pady=(0, 5))

    def _on_click(self, item):
        if self.command:
            self.command(item)

class Tabs(FluentWidget):
    def __init__(self, master=None, tabs=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.tabs = tabs or []
        self.command = command
        self.widget = ttk.Notebook(master, style="Fluent.TNotebook")
        self._create_tabs()

    def create_widget(self):
        return self.widget

    def _create_tabs(self):
        for tab in self.tabs:
            frame = ttk.Frame(self.widget, style="Fluent.TFrame")
            self.widget.add(frame, text=tab['text'])
            if 'content' in tab:
                tab['content'](frame)

        self.widget.bind("<<NotebookTabChanged>>", self._on_tab_change)

    def _on_tab_change(self, event):
        if self.command:
            current_tab = self.widget.index(self.widget.select())
            self.command(self.tabs[current_tab])
