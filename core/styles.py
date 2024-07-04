import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

COLORS = {
    'primary': '#0078d4',
    'secondary': '#2b88d8',
    'success': '#107c10',
    'warning': '#ffb900',
    'error': '#d83b01',
    'black': '#000000',
    'white': '#ffffff',
    'gray': '#605e5c',
    'light_gray': '#f3f2f1',
}

FONT_SIZES = {
    'tiny': 8,
    'small': 10,
    'medium': 12,
    'large': 14,
    'extra_large': 18,
    'huge': 24,
}

class ThemeManager:
    _current_theme = {}

    @classmethod
    def set_theme(cls, theme):
        cls._current_theme = theme

    @classmethod
    def get_current_theme(cls):
        return cls._current_theme

def apply_theme(component, theme=None):
    if theme is None:
        theme = ThemeManager.get_current_theme()

    if not theme:
        return

    if isinstance(component, tk.Widget):
        widget = component
    elif hasattr(component, 'widget'):
        widget = component.widget
    else:
        return

    bg_color = theme.get('colors', {}).get('background', COLORS['white'])
    fg_color = theme.get('colors', {}).get('foreground', COLORS['black'])
    font_family = theme.get('fonts', {}).get('primary', 'Segoe UI')
    font_size = theme.get('font_sizes', {}).get('medium', FONT_SIZES['medium'])

    widget.configure(bg=bg_color, fg=fg_color)

    custom_font = tkfont.Font(family=font_family, size=font_size)
    widget.configure(font=custom_font)

    if isinstance(widget, ttk.Widget):
        style = ttk.Style()
        style.configure(f'{widget.winfo_class()}.TWidget', background=bg_color, foreground=fg_color)
        widget.configure(style=f'{widget.winfo_class()}.TWidget')

def create_style(bg_color=None, fg_color=None, font_family=None, font_size=None):
    style = {}
    if bg_color:
        style['background'] = bg_color
    if fg_color:
        style['foreground'] = fg_color
    if font_family or font_size:
        font = tkfont.Font(family=font_family or 'Segoe UI', size=font_size or FONT_SIZES['medium'])
        style['font'] = font
    return style
