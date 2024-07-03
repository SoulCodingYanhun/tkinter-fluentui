from ..core.styles import COLORS, FONT_SIZES, FONT_WEIGHTS, SPACING

DEFAULT_THEME = {
    'name': 'default',
    'colors': {
        'primary': COLORS['primary'],
        'secondary': COLORS['secondary'],
        'background': COLORS['white'],
        'surface': COLORS['light'],
        'error': COLORS['danger'],
        'text': COLORS['black'],
        'on_primary': COLORS['white'],
        'on_secondary': COLORS['white'],
        'on_background': COLORS['black'],
        'on_surface': COLORS['black'],
        'on_error': COLORS['white'],
    },
    'typography': {
        'font_family': 'Segoe UI',
        'font_size': FONT_SIZES['md'],
        'font_weight': FONT_WEIGHTS['normal'],
        'line_height': 1.5,
        'heading': {
            'font_family': 'Segoe UI',
            'font_weight': FONT_WEIGHTS['semibold'],
            'line_height': 1.2,
            'h1': FONT_SIZES['4xl'],
            'h2': FONT_SIZES['3xl'],
            'h3': FONT_SIZES['2xl'],
            'h4': FONT_SIZES['xl'],
            'h5': FONT_SIZES['lg'],
            'h6': FONT_SIZES['md'],
        },
    },
    'shape': {
        'border_radius': 4,
        'border_width': 1,
    },
    'spacing': SPACING,
    'shadows': {
        'small': '0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)',
        'medium': '0 3px 6px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.12)',
        'large': '0 10px 20px rgba(0,0,0,0.15), 0 3px 6px rgba(0,0,0,0.10)',
    },
    'components': {
        'button': {
            'background': COLORS['primary'],
            'text': COLORS['white'],
            'hover': {
                'background': COLORS['primary_dark'],
                'text': COLORS['white'],
            },
            'active': {
                'background': COLORS['primary_dark'],
                'text': COLORS['white'],
            },
            'disabled': {
                'background': COLORS['gray_light'],
                'text': COLORS['gray'],
            },
        },
        'input': {
            'background': COLORS['white'],
            'text': COLORS['black'],
            'border': COLORS['gray_light'],
            'focus': {
                'border': COLORS['primary'],
            },
            'placeholder': COLORS['gray'],
        },
        # Add more component-specific styles here
    },
}
