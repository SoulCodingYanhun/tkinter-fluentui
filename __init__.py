"""
tkinter_fluentui - A Fluent UI inspired widget library for tkinter
"""

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
    'Skeleton'
]

def init(theme='default'):
    """
    Initialize the tkinter_fluentui library with the specified theme.
    
    :param theme: The name of the theme to use ('default' or 'dark'), or a CustomTheme object
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
    
    print(f"tkinter_fluentui initialized with {theme} theme.")

# Optional: Add any global configuration or setup here
def set_global_styles():
    """
    Set any global styles or configurations for the library.
    This function can be called after init() if needed.
    """
    # Add any global style settings here
    pass

# Optional: Add any cleanup or shutdown functions here
def shutdown():
    """
    Perform any necessary cleanup when shutting down the application.
    """
    # Add any cleanup code here
    pass

# If you want to perform any actions when the module is imported, you can add them here
print(f"tkinter_fluentui version {__version__} imported.")
