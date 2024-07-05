from typing import Dict, Any

class CustomTheme:
    def __init__(self):
        self.theme: Dict[str, Any] = {
            'name': 'custom',
            'TButton': {},
            'TEntry': {},
            'TFrame': {},
            'TLabel': {},
            'Horizontal.TProgressbar': {},
            'TCheckbutton': {}
        }

    def set_button_style(self, background: str, foreground: str, active_bg: str, font: tuple):
        self.theme['TButton'] = {
            'configure': {
                'background': background,
                'foreground': foreground,
                'font': font,
                'borderwidth': 0,
                'focuscolor': active_bg,
                'padding': (10, 5)
            },
            'map': {
                'background': [('active', active_bg)]
            }
        }

    def set_entry_style(self, background: str, foreground: str, border_color: str, font: tuple):
        self.theme['TEntry'] = {
            'configure': {
                'fieldbackground': background,
                'foreground': foreground,
                'font': font,
                'borderwidth': 1,
                'bordercolor': border_color,
                'padding': 5
            },
            'map': {
                'bordercolor': [('focus', border_color)]
            }
        }

    def set_frame_style(self, background: str):
        self.theme['TFrame'] = {
            'configure': {
                'background': background
            }
        }

    def set_label_style(self, background: str, foreground: str, font: tuple):
        self.theme['TLabel'] = {
            'configure': {
                'background': background,
                'foreground': foreground,
                'font': font
            }
        }

    def set_progressbar_style(self, trough_color: str, bar_color: str):
        self.theme['Horizontal.TProgressbar'] = {
            'configure': {
                'troughcolor': trough_color,
                'background': bar_color
            }
        }

    def set_checkbutton_style(self, background: str, foreground: str, font: tuple, indicator_color: str):
        self.theme['TCheckbutton'] = {
            'configure': {
                'background': background,
                'foreground': foreground,
                'font': font
            },
            'map': {
                'background': [('active', background)],
                'indicatorcolor': [('selected', indicator_color), ('!selected', background)],
                'indicatorbackground': [('selected', background), ('!selected', background)]
            }
        }

    def get_theme(self) -> Dict[str, Any]:
        return self.theme