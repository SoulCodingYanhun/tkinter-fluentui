import tkinter as tk
import tkinter.font as tkfont
from typing import List

def get_system_fonts() -> List[str]:
    """
    Get a list of available system fonts.
    """
    root = tk.Tk()
    fonts = list(tkfont.families())
    root.destroy()
    return sorted(fonts)

def measure_text_width(text: str, font: tuple) -> int:
    """
    Measure the width of a text string in pixels.
    """
    root = tk.Tk()
    label = tk.Label(root, text=text, font=font)
    width = label.winfo_reqwidth()
    root.destroy()
    return width

def create_font(family: str, size: int, weight: str = 'normal', slant: str = 'roman') -> tkfont.Font:
    """
    Create a font object.
    """
    return tkfont.Font(family=family, size=size, weight=weight, slant=slant)

def get_font_metrics(font: tkfont.Font) -> dict:
    """
    Get metrics for a font.
    """
    return {
        'ascent': font.metrics('ascent'),
        'descent': font.metrics('descent'),
        'linespace': font.metrics('linespace'),
        'fixed': font.metrics('fixed')
    }
