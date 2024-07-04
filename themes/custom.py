def create_custom_theme(**kwargs):
    custom_theme = {
        'colors': {
            'primary': '#0078d4',
            'secondary': '#2b88d8',
            'background': '#ffffff',
            'foreground': '#000000',
            'success': '#107c10',
            'warning': '#ffb900',
            'error': '#d83b01',
        },
        'fonts': {
            'primary': 'Segoe UI',
            'secondary': 'Arial',
        },
        'font_sizes': {
            'small': 10,
            'medium': 12,
            'large': 14,
        },
    }

    for key, value in kwargs.items():
        if key in custom_theme:
            custom_theme[key].update(value)

    return custom_theme
