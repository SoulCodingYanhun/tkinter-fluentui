from typing import Tuple
import colorsys

def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    Convert a hex color string to RGB values.
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    """
    Convert RGB values to a hex color string.
    """
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def lighten_color(hex_color: str, amount: float = 0.1) -> str:
    """
    Lighten a color by the given amount.
    """
    rgb = hex_to_rgb(hex_color)
    hls = colorsys.rgb_to_hls(*[x/255.0 for x in rgb])
    lightened = colorsys.hls_to_rgb(hls[0], min(1, hls[1] + amount), hls[2])
    return rgb_to_hex(tuple(int(x*255) for x in lightened))

def darken_color(hex_color: str, amount: float = 0.1) -> str:
    """
    Darken a color by the given amount.
    """
    rgb = hex_to_rgb(hex_color)
    hls = colorsys.rgb_to_hls(*[x/255.0 for x in rgb])
    darkened = colorsys.hls_to_rgb(hls[0], max(0, hls[1] - amount), hls[2])
    return rgb_to_hex(tuple(int(x*255) for x in darkened))

def get_contrast_ratio(color1: str, color2: str) -> float:
    """
    Calculate the contrast ratio between two colors.
    """
    def luminance(color):
        rgb = hex_to_rgb(color)
        rgb = [x / 255.0 for x in rgb]
        rgb = [((x + 0.055) / 1.055) ** 2.4 if x > 0.03928 else x / 12.92 for x in rgb]
        return 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]

    l1 = luminance(color1)
    l2 = luminance(color2)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)

def is_dark_color(hex_color: str) -> bool:
    """
    Determine if a color is dark or light.
    """
    rgb = hex_to_rgb(hex_color)
    brightness = (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000
    return brightness < 128
