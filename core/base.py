 
import tkinter as tk
from typing import Optional, Dict, Any

class FluentComponent:
    def __init__(
        self,
        master: Optional[tk.Widget] = None,
        id: Optional[str] = None,
        className: Optional[str] = None,
        style: Optional[Dict[str, Any]] = None
    ):
        self.master = master
        self.id = id
        self.className = className
        self.style = style or {}
        self.widget: Optional[tk.Widget] = None

    def create_widget(self):
        raise NotImplementedError("Subclasses must implement create_widget method")

    def apply_style(self):
        if self.widget:
            for key, value in self.style.items():
                try:
                    self.widget[key] = value
                except tk.TclError:
                    print(f"Warning: Unable to set style '{key}' for {self.__class__.__name__}")

    def pack(self, **kwargs):
        if self.widget:
            self.widget.pack(**kwargs)

    def grid(self, **kwargs):
        if self.widget:
            self.widget.grid(**kwargs)

    def place(self, **kwargs):
        if self.widget:
            self.widget.place(**kwargs)

    def destroy(self):
        if self.widget:
            self.widget.destroy()
            self.widget = None

    def update(self):
        if self.widget:
            self.widget.update()

    def bind(self, sequence, func, add=None):
        if self.widget:
            self.widget.bind(sequence, func, add)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, className={self.className})"
