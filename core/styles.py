from tkinter import ttk
from typing import Dict, Any

class FluentStyle:
    def __init__(self):
        self.style = ttk.Style()
        self._current_theme = "default"

    def configure(self, style_name: str, **kwargs):
        self.style.configure(style_name, **kwargs)

    def map(self, style_name: str, **kwargs):
        self.style.map(style_name, **kwargs)

    def layout(self, style_name: str, layout_spec):
        self.style.layout(style_name, layout_spec)

    def apply_theme(self, theme: Dict[str, Any]):
        for style_name, config in theme.items():
            if 'configure' in config:
                self.configure(style_name, **config['configure'])
            if 'map' in config:
                self.map(style_name, **config['map'])
            if 'layout' in config:
                self.layout(style_name, config['layout'])
        self._current_theme = theme.get('name', 'custom')

    def get_current_theme(self) -> str:
        return self._current_theme

fluent_style = FluentStyle()

def apply_theme(theme: Dict[str, Any]):
    fluent_style.apply_theme(theme)

def get_current_theme() -> str:
    return fluent_style.get_current_theme()
