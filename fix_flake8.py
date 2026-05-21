import re

with open("src/protontricks/gui.py", "r") as f:
    content = f.read()

# E302
content = content.replace("APP_ICON_SIZE = (32, 32)\n@dataclass", "APP_ICON_SIZE = (32, 32)\n\n\n@dataclass")

# Line too long 184 & 198
old_line_1 = '            "--title", title, "--width", str(options.width), "--height", str(options.height),'
new_line_1 = '            "--title", title, "--width", str(options.width),\n            "--height", str(options.height),'
content = content.replace(old_line_1, new_line_1)

old_line_2 = '            str(options.height), "--cancel-label", options.cancel_label, "--ok-label", options.ok_label'
new_line_2 = '            str(options.height), "--cancel-label", options.cancel_label,\n            "--ok-label", options.ok_label'
content = content.replace(old_line_2, new_line_2)

with open("src/protontricks/gui.py", "w") as f:
    f.write(content)
