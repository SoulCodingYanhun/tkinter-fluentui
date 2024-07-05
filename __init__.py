import tkinter as tk
from tkinter import ttk

# 导入核心模块
from .core import FluentComponent, FluentFrame, FluentWidget, FluentStyle, apply_theme, get_current_theme

# 导入主题模块
from .themes import DEFAULT_THEME, DARK_THEME, CustomTheme, get_theme, add_theme, list_themes

# 导入工具函数
from .utils import (
    announce, set_aria_label, set_aria_description, enable_screen_reader, disable_screen_reader,
    is_screen_reader_enabled, generate_id, format_date, debounce, throttle, create_font,
    get_widget_width, get_widget_height, center_window, create_tooltip, validate_email,
    limit_text_length, rgb_to_hex, hex_to_rgb
)

# 导入组件
from .components.buttons import Button, LinkButton
from .components.inputs import TextInput, SearchBox
from .components.selectors import Checkbox, RadioGroup, Dropdown, Slider, Switch, ColorPicker
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
from .components.pickers import FloatingPicker, ExtendedPicker
from .components.annotations import Annotation, Coachmark

__version__ = '0.1.0'


def init(theme='default', use_ttk=True):
    """
    初始化 tkinter_fluentui 库
    :param theme: 主题名称或主题字典
    :param use_ttk: 是否使用 ttk 小部件（默认为 True）
    """
    if isinstance(theme, str):
        theme_dict = get_theme(theme)
    elif isinstance(theme, dict):
        theme_dict = theme
    else:
        raise ValueError("Theme must be a string or a dictionary")

    apply_theme(theme_dict)

    if use_ttk:
        # 替换 tkinter 的基本小部件为 ttk 版本
        tk.Button = ttk.Button
        tk.Checkbutton = ttk.Checkbutton
        tk.Entry = ttk.Entry
        tk.Frame = ttk.Frame
        tk.Label = ttk.Label
        tk.LabelFrame = ttk.LabelFrame
        tk.Menubutton = ttk.Menubutton
        tk.PanedWindow = ttk.PanedWindow
        tk.Radiobutton = ttk.Radiobutton
        tk.Scale = ttk.Scale
        tk.Scrollbar = ttk.Scrollbar
        tk.Spinbox = ttk.Spinbox
        tk.Combobox = ttk.Combobox
        tk.Notebook = ttk.Notebook
        tk.Progressbar = ttk.Progressbar
        tk.Separator = ttk.Separator
        tk.Sizegrip = ttk.Sizegrip
        tk.Treeview = ttk.Treeview


# 在导入时自动初始化默认主题
init()

__all__ = [
    # 核心类
    'FluentComponent', 'FluentFrame', 'FluentWidget', 'FluentStyle',

    # 主题相关
    'DEFAULT_THEME', 'DARK_THEME', 'CustomTheme', 'get_theme', 'add_theme', 'list_themes',
    'apply_theme', 'get_current_theme',

    # 工具函数
    'announce', 'set_aria_label', 'set_aria_description', 'enable_screen_reader',
    'disable_screen_reader', 'is_screen_reader_enabled', 'generate_id', 'format_date',
    'debounce', 'throttle', 'create_font', 'get_widget_width', 'get_widget_height',
    'center_window', 'create_tooltip', 'validate_email', 'limit_text_length',
    'rgb_to_hex', 'hex_to_rgb',

    # 组件
    'Button', 'LinkButton', 'TextInput', 'SearchBox', 'Checkbox', 'RadioGroup',
    'Dropdown', 'Slider', 'Switch', 'ColorPicker', 'DetailsList', 'GroupedList',
    'List', 'Breadcrumb', 'CommandBar', 'NavMenu', 'Tabs', 'ProgressBar', 'Spinner',
    'Dialog', 'Modal', 'MessageBar', 'TeachingBubble', 'Tooltip', 'Panel', 'Form',
    'Calendar', 'DatePicker', 'PersonaGroup', 'PersonCard', 'Image', 'Icon', 'Stack',
    'Label', 'Text', 'Separator', 'Skeleton', 'FloatingPicker', 'ExtendedPicker',
    'Annotation', 'Coachmark',

    # 初始化函数
    'init'
]
