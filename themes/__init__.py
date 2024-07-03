from .default import DEFAULT_THEME
from .dark import DARK_THEME
from .custom import CustomTheme

__all__ = ['DEFAULT_THEME', 'DARK_THEME', 'CustomTheme', 'get_theme', 'set_theme', 'create_theme']

_current_theme = DEFAULT_THEME

def get_theme():
    global _current_theme
    return _current_theme

def set_theme(theme):
    global _current_theme
    if isinstance(theme, dict):
        _current_theme = theme
    elif theme == 'dark':
        _current_theme = DARK_THEME
    elif theme == 'default':
        _current_theme = DEFAULT_THEME
    else:
        raise ValueError("Invalid theme. Use 'default', 'dark', or a custom theme dict.")

def create_theme(name, base_theme='default', **kwargs):
    base = DEFAULT_THEME if base_theme == 'default' else DARK_THEME
    new_theme = base.copy()
    new_theme.update(kwargs)
    return CustomTheme(name, new_theme)
