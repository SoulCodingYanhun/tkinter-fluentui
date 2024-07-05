DARK_THEME = {
    'name': 'dark',
    'TButton': {
        'configure': {
            'background': '#0078d4',
            'foreground': 'white',
            'font': ('Segoe UI', 10),
            'borderwidth': 0,
            'focuscolor': '#005a9e',
            'padding': (10, 5)
        },
        'map': {
            'background': [('active', '#106ebe'), ('disabled', '#3b3a39')],
            'foreground': [('disabled', '#a19f9d')]
        }
    },
    'TEntry': {
        'configure': {
            'fieldbackground': '#292827',
            'foreground': 'white',
            'font': ('Segoe UI', 10),
            'borderwidth': 1,
            'bordercolor': '#8a8886',
            'padding': 5
        },
        'map': {
            'bordercolor': [('focus', '#0078d4')]
        }
    },
    'TFrame': {
        'configure': {
            'background': '#201f1e'
        }
    },
    'TLabel': {
        'configure': {
            'background': '#201f1e',
            'foreground': '#ffffff',
            'font': ('Segoe UI', 10)
        }
    },
    'Horizontal.TProgressbar': {
        'configure': {
            'troughcolor': '#3b3a39',
            'background': '#0078d4'
        }
    },
    'TCheckbutton': {
        'configure': {
            'background': '#201f1e',
            'foreground': '#ffffff',
            'font': ('Segoe UI', 10)
        },
        'map': {
            'background': [('active', '#323130')],
            'indicatorcolor': [('selected', '#0078d4'), ('!selected', '#201f1e')],
            'indicatorbackground': [('selected', '#201f1e'), ('!selected', '#201f1e')]
        }
    }
}
