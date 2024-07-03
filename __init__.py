"""
tkinter_fluentui - A Fluent UI inspired widget library for tkinter
"""

import tkinter as tk
from tkinter import font as tkfont
import sys

# Version of the tkinter_fluentui package
__version__ = "0.1.0"

# Import core modules
from .core import FluentComponent, ThemeManager

# Import themes
from .themes import DEFAULT_THEME, DARK_THEME, CustomTheme, get_theme, set_theme, create_theme

# Import utility functions
from .utils import (
    announce_for_screen_readers,
    set_aria_label,
    generate_id,
    format_date,
    debounce,
    throttle,
    lighten_color,
    darken_color,
    get_contrast_ratio,
    is_dark_color,
    get_system_fonts,
    measure_text_width
)

# Import components
from .components.buttons import Button, LinkButton
from .components.inputs import TextInput, PasswordInput, SearchBox
from .components.selectors import (
    Checkbox,
    RadioButton,
    RadioGroup,
    Dropdown,
    Slider,
    Switch,
    ColorPicker
)
from .components.lists import DetailsList, GroupedList, List
from .components.navigation import Breadcrumb, CommandBar, NavMenu, Tabs
from .components.progress import ProgressBar, Spinner
from .components.dialogs import Dialog, Modal
from .components.notifications import MessageBar, TeachingBubble, Tooltip
from .components.panels import Panel
from .components.forms import Form
from .components.date_time import Calendar, DatePicker
from .components.people import PersonaGroup, PersonCard
from .components.media import Image, Icon
from .components.layout import Stack
from .components.text import Label, Text
from .components.misc import Separator, Skeleton

# Global configuration dictionary
GLOBAL_CONFIG = {
    'font_family': 'Segoe UI',
    'font_size': 12,
    'animation_duration': 200,
    'tooltip_delay': 500,
    'use_system_accent_color': False,
    'enable_animations': True,
    'enable_sounds': False,
    'high_contrast_mode': False
}

def set_global_styles(
    font_family: str = None,
    font_size: int = None,
    animation_duration: int = None,
    tooltip_delay: int = None,
    use_system_accent_color: bool = None,
    enable_animations: bool = None,
    enable_sounds: bool = None,
    high_contrast_mode: bool = None
):
    """
    Set global styles and configurations for the library.
    This function can be called after init() if needed.

    :param font_family: The default font family to use for all widgets
    :param font_size: The default font size to use for all widgets
    :param animation_duration: The duration of animations in milliseconds
    :param tooltip_delay: The delay before tooltips appear, in milliseconds
    :param use_system_accent_color: Whether to use the system's accent color
    :param enable_animations: Whether to enable animations globally
    :param enable_sounds: Whether to enable sound effects
    :param high_contrast_mode: Whether to use high contrast mode for accessibility
    """
    global GLOBAL_CONFIG

    if font_family is not None:
        if font_family in get_system_fonts():
            GLOBAL_CONFIG['font_family'] = font_family
        else:
            print(f"Warning: Font '{font_family}' not found. Using default.")

    if font_size is not None:
        GLOBAL_CONFIG['font_size'] = font_size

    if animation_duration is not None:
        GLOBAL_CONFIG['animation_duration'] = animation_duration

    if tooltip_delay is not None:
        GLOBAL_CONFIG['tooltip_delay'] = tooltip_delay

    if use_system_accent_color is not None:
        GLOBAL_CONFIG['use_system_accent_color'] = use_system_accent_color

    if enable_animations is not None:
        GLOBAL_CONFIG['enable_animations'] = enable_animations

    if enable_sounds is not None:
        GLOBAL_CONFIG['enable_sounds'] = enable_sounds

    if high_contrast_mode is not None:
        GLOBAL_CONFIG['high_contrast_mode'] = high_contrast_mode

    _apply_global_styles()

def _apply_global_styles():
    """
    Apply the global styles to all widgets and update the theme.
    """
    # Set default font
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(family=GLOBAL_CONFIG['font_family'], size=GLOBAL_CONFIG['font_size'])

    # Update theme with new global configurations
    current_theme = ThemeManager.get_current_theme()
    current_theme.update({
        'font_family': GLOBAL_CONFIG['font_family'],
        'font_size': GLOBAL_CONFIG['font_size'],
        'animation_duration': GLOBAL_CONFIG['animation_duration'],
        'tooltip_delay': GLOBAL_CONFIG['tooltip_delay'],
        'high_contrast_mode': GLOBAL_CONFIG['high_contrast_mode']
    })

    if GLOBAL_CONFIG['use_system_accent_color']:
        system_accent_color = _get_system_accent_color()
        current_theme['colors']['primary'] = system_accent_color

    ThemeManager.set_theme(current_theme)

    # Apply high contrast mode if enabled
    if GLOBAL_CONFIG['high_contrast_mode']:
        _apply_high_contrast_mode()

def _get_system_accent_color():
    """
    Get the system accent color.
    This is a placeholder function and should be implemented based on the target platform.
    """
    if sys.platform == 'win32':
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Accent")
            accent_palette = winreg.QueryValueEx(key, "AccentPalette")[0]
            return f"#{accent_palette[8:11].hex()}"
        except:
            pass
    return "#0078D7"  # Default Windows 10 accent color

def _apply_high_contrast_mode():
    """
    Apply high contrast mode to the current theme.
    """
    current_theme = ThemeManager.get_current_theme()
    # Modify theme colors for high contrast
    current_theme['colors'].update({
        'background': '#000000',
        'foreground': '#FFFFFF',
        'primary': '#FFFF00',
        'secondary': '#00FFFF',
    })
    ThemeManager.set_theme(current_theme)

def get_global_config(key: str):
    """
    Get a global configuration value.

    :param key: The configuration key
    :return: The configuration value
    """
    return GLOBAL_CONFIG.get(key)

def init(theme='default', **global_style_options):
    """
    Initialize the tkinter_fluentui library with the specified theme and global styles.
    
    :param theme: The name of the theme to use ('default' or 'dark'), or a CustomTheme object
    :param global_style_options: Additional keyword arguments for global styles
    """
    if isinstance(theme, str):
        if theme.lower() == 'default':
            set_theme(DEFAULT_THEME)
        elif theme.lower() == 'dark':
            set_theme(DARK_THEME)
        else:
            raise ValueError("Invalid theme name. Use 'default', 'dark', or a CustomTheme object.")
    elif isinstance(theme, CustomTheme):
        set_theme(theme)
    else:
        raise TypeError("Theme must be a string ('default' or 'dark') or a CustomTheme object.")
    
    # Apply global styles
    set_global_styles(**global_style_options)
    
    print(f"tkinter_fluentui version {__version__} initialized with {theme} theme and custom global styles.")

def shutdown():
    """
    Perform any necessary cleanup when shutting down the application.
    """
    # Add any cleanup code here
    print("Shutting down tkinter_fluentui...")

# Define __all__ to specify what gets imported with wildcard imports
__all__ = [
    # Core
    'FluentComponent',
    'ThemeManager',
    
    # Themes
    'DEFAULT_THEME',
    'DARK_THEME',
    'CustomTheme',
    'get_theme',
    'set_theme',
    'create_theme',
    
    # Utility functions
    'announce_for_screen_readers',
    'set_aria_label',
    'generate_id',
    'format_date',
    'debounce',
    'throttle',
    'lighten_color',
    'darken_color',
    'get_contrast_ratio',
    'is_dark_color',
    'get_system_fonts',
    'measure_text_width',
    
    # Components
    'Button',
    'LinkButton',
    'TextInput',
    'PasswordInput',
    'SearchBox',
    'Checkbox',
    'RadioButton',
    'RadioGroup',
    'Dropdown',
    'Slider',
    'Switch',
    'ColorPicker',
    'DetailsList',
    'GroupedList',
    'List',
    'Breadcrumb',
    'CommandBar',
    'NavMenu',
    'Tabs',
    'ProgressBar',
    'Spinner',
    'Dialog',
    'Modal',
    'MessageBar',
    'TeachingBubble',
    'Tooltip',
    'Panel',
    'Form',
    'Calendar',
    'DatePicker',
    'PersonaGroup',
    'PersonCard',
    'Image',
    'Icon',
    'Stack',
    'Label',
    'Text',
    'Separator',
    'Skeleton',
    
    # Global configuration
    'set_global_styles',
    'get_global_config',
    'init',
    'shutdown'
]

# If you want to perform any actions when the module is imported, you can add them here
print(f"tkinter_fluentui version {__version__} imported. Call init() to set up the library.")
