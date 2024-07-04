import tkinter as tk
from tkinter import ttk
import sys

# 导入核心模块
from .core.base import FluentComponent
from .core.styles import apply_theme, COLORS, FONT_SIZES

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

# 导入主题
from .themes import set_theme, get_current_theme
from .themes.default import DEFAULT_THEME
from .themes.dark import DARK_THEME

# 导入工具函数
from .utils import accessibility, helpers

__version__ = '0.1.0'


def init(theme='default', master=None):
    """
    初始化 tkinter_fluentui 库。
    
    :param theme: 要使用的主题名称，默认为 'default'
    :param master: tkinter 主窗口，如果为 None 则创建一个新窗口
    :return: 初始化后的主窗口
    """
    if master is None:
        master = tk.Tk()

    if theme == 'default':
        set_theme(DEFAULT_THEME)
    elif theme == 'dark':
        set_theme(DARK_THEME)
    else:
        raise ValueError(f"Unsupported theme: {theme}")

    style = ttk.Style()
    style.theme_use('clam')  # 使用 'clam' 主题作为基础

    # 配置全局字体
    default_font = ('Segoe UI', 10)
    master.option_add('*Font', default_font)

    # 配置全局颜色
    master.configure(bg=get_current_theme()['colors']['background'])

    # 设置 DPI 感知（仅在 Windows 上）
    if sys.platform.startswith('win'):
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except ImportError:
            print("无法导入 ctypes 模块，DPI 感知可能无法正常工作。")
        except AttributeError:
            print("无法设置 DPI 感知，可能是 Windows 版本不支持此功能。")
        except Exception as e:
            print(f"设置 DPI 感知时发生未知错误: {e}")

    return master


# 导出所有公共组件和函数
__all__ = [
    'FluentComponent', 'apply_theme', 'COLORS', 'FONT_SIZES',
    'Button', 'LinkButton', 'TextInput', 'SearchBox',
    'Checkbox', 'RadioGroup', 'Dropdown', 'Slider', 'Switch', 'ColorPicker',
    'DetailsList', 'GroupedList', 'List',
    'Breadcrumb', 'CommandBar', 'NavMenu', 'Tabs',
    'ProgressBar', 'Spinner',
    'Dialog', 'Modal',
    'MessageBar', 'TeachingBubble', 'Tooltip',
    'Panel', 'Form',
    'Calendar', 'DatePicker',
    'PersonaGroup', 'PersonCard',
    'Image', 'Icon',
    'Stack',
    'Label', 'Text',
    'Separator', 'Skeleton',
    'FloatingPicker', 'ExtendedPicker',
    'Annotation', 'Coachmark',
    'set_theme', 'get_current_theme',
    'accessibility', 'helpers',
    'init'
]
