with open("src/protontricks/gui.py", "r") as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if i == 23 and line.startswith("@dataclass"):
        new_lines.insert(-1, "\n")
    new_lines.append(line)

with open("src/protontricks/gui.py", "w") as f:
    f.writelines(new_lines)
