from .default import DEFAULT_THEME
from .dark import DARK_THEME
from .custom import CustomTheme

__all__ = ['DEFAULT_THEME', 'DARK_THEME', 'CustomTheme']

# 全局主题字典
THEMES = {
    'default': DEFAULT_THEME,
    'dark': DARK_THEME
}

def get_theme(name: str):
    """获取指定名称的主题"""
    return THEMES.get(name, DEFAULT_THEME)

def add_theme(name: str, theme: dict):
    """添加新主题"""
    THEMES[name] = theme

def list_themes():
    """列出所有可用主题"""
    return list(THEMES.keys())
