import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget


class FloatingPicker(FluentWidget):
    def __init__(self, master=None, options=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.options = options or []
        self.command = command
        self.widget = ttk.Frame(master)
        self._create_picker()

    def create_widget(self):
        return self.widget

    def _create_picker(self):
        self.var = tk.StringVar()
        self.combobox = ttk.Combobox(self.widget, textvariable=self.var, values=self.options, style="Fluent.TCombobox")
        self.combobox.pack(side=tk.LEFT)
        self.combobox.bind("<<ComboboxSelected>>", self._on_select)

    def _on_select(self, event):
        if self.command:
            self.command(self.var.get())

    def get(self):
        return self.var.get()

    def set(self, value):
        self.var.set(value)


class ExtendedPicker(FluentWidget):
    def __init__(self, master=None, options=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.options = options or []
        self.command = command
        self.widget = ttk.Frame(master)
        self._create_picker()

    def create_widget(self):
        return self.widget

    def _create_picker(self):
        self.listbox = tk.Listbox(self.widget, selectmode=tk.MULTIPLE, exportselection=0)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        for option in self.options:
            self.listbox.insert(tk.END, option)

        scrollbar = ttk.Scrollbar(self.widget, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.listbox.bind("<<ListboxSelect>>", self._on_select)

    def _on_select(self, event):
        if self.command:
            self.command(self.get())

    def get(self):
        return [self.listbox.get(i) for i in self.listbox.curselection()]

    def set(self, values):
        self.listbox.selection_clear(0, tk.END)
        for index, item in enumerate(self.listbox.get(0, tk.END)):
            if item in values:
                self.listbox.selection_set(index)
