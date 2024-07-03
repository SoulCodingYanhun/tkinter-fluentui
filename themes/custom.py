class CustomTheme:
    def __init__(self, name, theme_dict):
        self.name = name
        self.theme = theme_dict

    def __getitem__(self, key):
        return self.theme[key]

    def __setitem__(self, key, value):
        self.theme[key] = value

    def get(self, key, default=None):
        return self.theme.get(key, default)

    def update(self, **kwargs):
        self.theme.update(kwargs)

    def copy(self):
        return CustomTheme(f"{self.name}_copy", self.theme.copy())

    def __repr__(self):
        return f"CustomTheme(name='{self.name}')"

def create_custom_theme(name, base_theme, **overrides):
    new_theme = base_theme.copy()
    new_theme.update(overrides)
    return CustomTheme(name, new_theme)
