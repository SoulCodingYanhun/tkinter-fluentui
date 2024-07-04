from .default import DEFAULT_THEME
from .dark import DARK_THEME
from ..core.styles import ThemeManager

def set_theme(theme_name):
    if theme_name == 'default':
        ThemeManager.set_theme(DEFAULT_THEME)
    elif theme_name == 'dark':
        ThemeManager.set_theme(DARK_THEME)
    else:
        raise ValueError(f"Unknown theme: {theme_name}")

def get_current_theme():
    return ThemeManager.get_current_theme()

__all__ = ['DEFAULT_THEME', 'DARK_THEME', 'set_theme', 'get_current_theme']
