 
# core/__init__.py

from .base import FluentComponent
from .styles import (
    COLORS,
    FONT_SIZES,
    FONT_WEIGHTS,
    SPACING,
    create_font,
    create_button_style,
    DEFAULT_BUTTON_STYLE,
    apply_theme,
    ThemeManager,
    get_system_font_families,
    create_style_class
)

__all__ = [
    'FluentComponent',
    'COLORS',
    'FONT_SIZES',
    'FONT_WEIGHTS',
    'SPACING',
    'create_font',
    'create_button_style',
    'DEFAULT_BUTTON_STYLE',
    'apply_theme',
    'ThemeManager',
    'get_system_font_families',
    'create_style_class'
]

def initialize_core():
    """
    Initialize the core module. This function can be used to perform any necessary
    setup when the core module is first imported.
    """
    # You can add any initialization code here if needed
    print("Initializing tkinter_fluentui core module...")
    
    # For example, you might want to set up a default theme:
    ThemeManager.set_theme('default')

# Call the initialization function
initialize_core()

# Version information
__version__ = "0.1.0"

def get_version():
    """
    Return the version of the core module.
    """
    return __version__

# You can add more utility functions here if needed

def is_dark_mode():
    """
    Check if the current theme is in dark mode.
    This is a placeholder function and should be implemented based on your theming logic.
    """
    current_theme = ThemeManager.get_current_theme()
    # This is a simple check. You might want to implement a more sophisticated detection.
    return current_theme.get('bg_color', COLORS['white']) == COLORS['dark']

def set_dark_mode(enabled: bool):
    """
    Set the dark mode for the application.
    This is a placeholder function and should be implemented based on your theming logic.
    """
    if enabled:
        ThemeManager.set_theme('dark')  # Assuming you have a 'dark' theme defined
    else:
        ThemeManager.set_theme('default')  # Assuming 'default' is your light theme

# You can add more utility functions or classes here as needed
