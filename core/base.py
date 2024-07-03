import tkinter as tk
from typing import Optional, Dict, Any, List
import uuid

class FluentComponent:
    def __init__(
        self,
        master: Optional[tk.Widget] = None,
        id: Optional[str] = None,
        className: Optional[str] = None,
        style: Optional[Dict[str, Any]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        bg: Optional[str] = None,
        fg: Optional[str] = None,
        font: Optional[tuple] = None,
        cursor: Optional[str] = None,
    ):
        self.master = master
        self.id = id or str(uuid.uuid4())
        self.className = className
        self.style = style or {}
        self.width = width
        self.height = height
        self.padx = padx
        self.pady = pady
        self.bg = bg
        self.fg = fg
        self.font = font
        self.cursor = cursor
        self.widget: Optional[tk.Widget] = None
        self._event_bindings: List[tuple] = []

    def create_widget(self):
        raise NotImplementedError("Subclasses must implement create_widget method")

    def apply_style(self):
        if self.widget:
            style_attrs = {
                'width': self.width,
                'height': self.height,
                'padx': self.padx,
                'pady': self.pady,
                'bg': self.bg,
                'fg': self.fg,
                'font': self.font,
                'cursor': self.cursor,
            }
            style_attrs.update(self.style)
            
            for key, value in style_attrs.items():
                if value is not None:
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

    def bind(self, sequence: str, func, add: Optional[bool] = None):
        if self.widget:
            self.widget.bind(sequence, func, add)
            self._event_bindings.append((sequence, func, add))

    def unbind(self, sequence: str):
        if self.widget:
            self.widget.unbind(sequence)
            self._event_bindings = [b for b in self._event_bindings if b[0] != sequence]

    def rebind_events(self):
        for sequence, func, add in self._event_bindings:
            self.widget.bind(sequence, func, add)

    def set_style(self, **kwargs):
        self.style.update(kwargs)
        self.apply_style()

    def get_widget(self) -> Optional[tk.Widget]:
        return self.widget

    def set_state(self, state: str):
        if self.widget:
            self.widget.config(state=state)

    def get_state(self) -> str:
        if self.widget:
            return str(self.widget.cget('state'))
        return ''

    def focus(self):
        if self.widget:
            self.widget.focus_set()

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, className={self.className})"

    def __repr__(self):
        return self.__str__()
