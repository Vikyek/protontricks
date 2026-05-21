import re

with open("src/protontricks/gui.py", "r") as f:
    content = f.read()

content = content.replace("APP_ICON_SIZE = (32, 32)\n\n\n@dataclass", "APP_ICON_SIZE = (32, 32)\n\n\n@dataclass")

content = content.replace('    if options is None:\n        options = DialogOptions()\n\n    def _get_yad_args():', '    if options is None:\n        options = DialogOptions()\n\n    def _get_yad_args():')

old_def = """
def show_text_dialog(
        title,
        text,
        window_icon,
        options=None):"""

new_def = """

def show_text_dialog(
        title,
        text,
        window_icon,
        options=None):"""

content = content.replace(old_def, new_def)

with open("src/protontricks/gui.py", "w") as f:
    f.write(content)
