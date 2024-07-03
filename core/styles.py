from typing import Dict, Any, Tuple
import tkinter as tk
import tkinter.font as tkfont

COLORS = {
    'primary': '#0078d4',
    'primary_dark': '#005a9e',
    'primary_light': '#c7e0f4',
    'secondary': '#2b88d8',
    'secondary_dark': '#1f6bab',
    'secondary_light': '#d0e7f8',
    'success': '#107c10',
    'success_dark': '#0b5a0b',
    'success_light': '#c6e0c6',
    'danger': '#d13438',
    'danger_dark': '#a02a2d',
    'danger_light': '#f1d0d1',
    'warning': '#ffaa44',
    'warning_dark': '#d48c35',
    'warning_light': '#f9e8d2',
    'info': '#0098db',
    'info_dark': '#0072a3',
    'info_light': '#c5e8f7',
    'light': '#f3f2f1',
    'dark': '#252423',
    'white': '#ffffff',
    'black': '#000000',
    'gray': '#605e5c',
    'gray_light': '#d2d0ce',
    'transparent': 'transparent',
}

FONT_SIZES = {
    'xs': 10,
    'sm': 12,
    'md': 14,
    'lg': 16,
    'xl': 20,
    '2xl': 24,
    '3xl': 30,
    '4xl': 36,
}

FONT_WEIGHTS = {
    'light': 'light',
    'normal': 'normal',
    'medium': 'medium',
    'semibold': 'semibold',
    'bold': 'bold',
}

SPACING = {
    'xs': 4,
    'sm': 8,
    'md': 16,
    'lg': 24,
    'xl': 32,
    '2xl': 48,
    '3xl': 64,
}

def create_font(size: str = 'md', weight: str = 'normal', family: str = 'Segoe UI') -> Tuple[str, int, str]:
    return (family, FONT_SIZES[size], FONT_WEIGHTS[weight])

def create_button_style(
    bg_color: str,
    fg_color: str,
    hover_bg_color: str,
    hover_fg_color: str,
    active_bg_color: str,
    active_fg_color: str,
    disabled_bg_color: str,
    disabled_fg_color: str,
    font_size: str = 'md',
    font_weight: str = 'normal',
    padding_x: str = 'md',
    padding_y: str = 'sm',
    border_radius: int = 2
) -> Dict[str, Any]:
    return {
        'background': bg_color,
        'foreground': fg_color,
        'activebackground': active_bg_color,
        'activeforeground': active_fg_color,
        'disabledbackground': disabled_bg_color,
        'disabledforeground': disabled_fg_color,
        'font': create_font(font_size, font_weight),
        'padx': SPACING[padding_x],
        'pady': SPACING[padding_y],
        'borderwidth': 0,
        'relief': tk.FLAT,
        'highlightthickness': 0,
        'bd': 0,
        'cursor': 'hand2',
        'compound': tk.LEFT,
    }

DEFAULT_BUTTON_STYLE = create_button_style(
    bg_color=COLORS['primary'],
    fg_color=COLORS['white'],
    hover_bg_color=COLORS['primary_dark'],
    hover_fg_color=COLORS['white'],
    active_bg_color=COLORS['primary_dark'],
    active_fg_color=COLORS['white'],
    disabled_bg_color=COLORS['gray_light'],
    disabled_fg_color=COLORS['gray']
)

def apply_theme(component: 'FluentComponent', theme: Dict[str, Any]):
    if hasattr(component, 'style') and isinstance(component.style, dict):
        component.style.update(theme)
    if hasattr(component, 'apply_style'):
        component.apply_style()

class ThemeManager:
    _current_theme = 'default'
    _themes = {
        'default': {
            'bg_color': COLORS['white'],
            'fg_color': COLORS['black'],
            'accent_color': COLORS['primary'],
            'font_family': 'Segoe UI',
            'font_size': FONT_SIZES['md'],
        }
    }

    @classmethod
    def get_current_theme(cls) -> Dict[str, Any]:
        return cls._themes[cls._current_theme]

    @classmethod
    def set_theme(cls, theme_name: str):
        if theme_name in cls._themes:
            cls._current_theme = theme_name
        else:
            raise ValueError(f"Theme '{theme_name}' not found")

    @classmethod
    def add_theme(cls, name: str, theme: Dict[str, Any]):
        cls._themes[name] = theme

    @classmethod
    def get_color(cls, color_name: str) -> str:
        return cls.get_current_theme().get(color_name, COLORS.get(color_name, color_name))

def get_system_font_families() -> List[str]:
    return list(set(tkfont.families()))

def create_style_class(widget_type: str, **kwargs) -> str:
    style = tk.Style()
    class_name = f"{widget_type}.TCustom.{uuid.uuid4().hex[:8]}"
    style.configure(class_name, **kwargs)
    return class_name
