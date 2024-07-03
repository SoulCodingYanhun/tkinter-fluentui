from ..core.styles import COLORS, FONT_SIZES, FONT_WEIGHTS, SPACING

DARK_THEME = {
    'name': 'dark',
    'colors': {
        'primary': COLORS['primary_light'],
        'secondary': COLORS['secondary_light'],
        'background': COLORS['dark'],
        'surface': COLORS['gray'],
        'error': COLORS['danger_light'],
        'text': COLORS['white'],
        'on_primary': COLORS['black'],
        'on_secondary': COLORS['black'],
        'on_background': COLORS['white'],
        'on_surface': COLORS['white'],
        'on_error': COLORS['black'],
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
        'small': '0 1px 3px rgba(255,255,255,0.12), 0 1px 2px rgba(255,255,255,0.24)',
        'medium': '0 3px 6px rgba(255,255,255,0.15), 0 2px 4px rgba(255,255,255,0.12)',
        'large': '0 10px 20px rgba(255,255,255,0.15), 0 3px 6px rgba(255,255,255,0.10)',
    },
    'components': {
        'button': {
            'background': COLORS['primary_light'],
            'text': COLORS['black'],
            'hover': {
                'background': COLORS['primary'],
                'text': COLORS['black'],
            },
            'active': {
                'background': COLORS['primary'],
                'text': COLORS['black'],
            },
            'disabled': {
                'background': COLORS['gray'],
                'text': COLORS['gray_light'],
            },
        },
        'input': {
            'background': COLORS['gray'],
            'text': COLORS['white'],
            'border': COLORS['gray_light'],
            'focus': {
                'border': COLORS['primary_light'],
            },
            'placeholder': COLORS['gray_light'],
        },
        # Add more component-specific styles here
    },
}
