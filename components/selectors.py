import tkinter as tk
from tkinter import ttk
from ..core import FluentWidget
import colorsys

class Checkbox(FluentWidget):
    def __init__(self, master=None, text="", variable=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.variable = variable or tk.BooleanVar()
        self.command = command
        self.widget = ttk.Checkbutton(master, text=text, variable=self.variable, command=self._on_toggle, style="Fluent.TCheckbutton")

    def create_widget(self):
        return self.widget

    def _on_toggle(self):
        if self.command:
            self.command()

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class RadioGroup(FluentWidget):
    def __init__(self, master=None, options=None, variable=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.options = options or []
        self.variable = variable or tk.StringVar()
        self.command = command
        self.widget = ttk.Frame(master)
        self._create_radiobuttons()

    def create_widget(self):
        return self.widget

    def _create_radiobuttons(self):
        for option in self.options:
            rb = ttk.Radiobutton(self.widget, text=option, variable=self.variable, value=option, command=self._on_select, style="Fluent.TRadiobutton")
            rb.pack(anchor="w", padx=5, pady=2)

    def _on_select(self):
        if self.command:
            self.command()

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class Dropdown(FluentWidget):
    def __init__(self, master=None, options=None, variable=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.options = options or []
        self.variable = variable or tk.StringVar()
        self.command = command
        self.widget = ttk.Combobox(master, values=self.options, textvariable=self.variable, style="Fluent.TCombobox")
        self.widget.bind("<<ComboboxSelected>>", self._on_select)

    def create_widget(self):
        return self.widget

    def _on_select(self, event):
        if self.command:
            self.command()

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class Slider(FluentWidget):
    def __init__(self, master=None, from_=0, to=100, variable=None, command=None, orientation="horizontal", **kwargs):
        super().__init__(master, **kwargs)
        self.variable = variable or tk.DoubleVar()
        self.command = command
        self.widget = ttk.Scale(master, from_=from_, to=to, variable=self.variable, command=self._on_slide, orient=orientation, style="Fluent.TScale")

    def create_widget(self):
        return self.widget

    def _on_slide(self, value):
        if self.command:
            self.command(float(value))

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class Switch(FluentWidget):
    def __init__(self, master=None, text="", variable=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.variable = variable or tk.BooleanVar()
        self.command = command
        self.widget = ttk.Frame(master)
        self._create_switch()

    def create_widget(self):
        return self.widget

    def _create_switch(self):
        self.switch = ttk.Checkbutton(self.widget, style="Switch.TCheckbutton", variable=self.variable, command=self._on_toggle)
        self.switch.pack(side=tk.LEFT)
        if self.text:
            self.label = ttk.Label(self.widget, text=self.text)
            self.label.pack(side=tk.LEFT, padx=(5, 0))

    def _on_toggle(self):
        if self.command:
            self.command()

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class ColorPicker(FluentWidget):
    def __init__(self, master=None, color=None, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.color = color or "#000000"
        self.command = command
        self.widget = ttk.Frame(master)
        self._create_color_picker()

    def create_widget(self):
        return self.widget

    def _create_color_picker(self):
        self.color_display = tk.Canvas(self.widget, width=30, height=30, bg=self.color, highlightthickness=1, highlightbackground="black")
        self.color_display.pack(side=tk.LEFT)
        self.color_display.bind("<Button-1>", self._open_color_chooser)

        self.color_entry = ttk.Entry(self.widget, width=10)
        self.color_entry.pack(side=tk.LEFT, padx=(5, 0))
        self.color_entry.insert(0, self.color)
        self.color_entry.bind("<Return>", self._update_color_from_entry)
        self.color_entry.bind("<FocusOut>", self._update_color_from_entry)

    def _open_color_chooser(self, event):
        color = tk.colorchooser.askcolor(color=self.color, title="Choose color")
        if color[1]:
            self.set_color(color[1])

    def _update_color_from_entry(self, event):
        color = self.color_entry.get()
        if self._is_valid_color(color):
            self.set_color(color)
        else:
            self.color_entry.delete(0, tk.END)
            self.color_entry.insert(0, self.color)

    def _is_valid_color(self, color):
        return len(color) == 7 and color[0] == "#" and all(c in "0123456789ABCDEFabcdef" for c in color[1:])

    def set_color(self, color):
        self.color = color
        self.color_display.config(bg=color)
        self.color_entry.delete(0, tk.END)
        self.color_entry.insert(0, color)
        if self.command:
            self.command(color)

    def get_color(self):
        return self.color