import re

with open("src/protontricks/gui.py", "r") as f:
    content = f.read()

content = content.replace("from PIL import Image", "from dataclasses import dataclass\n\nfrom PIL import Image")

dialog_options = """
@dataclass
class DialogOptions:
    cancel_label: str = "Cancel"
    add_cancel_button: bool = False
    ok_label: str = "OK"
    width: int = 600
    height: int = 600
"""
content = content.replace("APP_ICON_SIZE = (32, 32)\n", "APP_ICON_SIZE = (32, 32)\n" + dialog_options)
content = content.replace('"LocaleError", "get_gui_provider", "select_steam_app_with_gui",', '"DialogOptions", "LocaleError", "get_gui_provider", "select_steam_app_with_gui",')


old_func = """def show_text_dialog(
        title,
        text,
        window_icon,
        cancel_label=None,
        add_cancel_button=False,
        ok_label=None,
        width=600,
        height=600):
    \"\"\"
    Show a text dialog to the user

    :returns: True if user clicked OK, False otherwise
    \"\"\"
    if not ok_label:
        ok_label = "OK"

    if not cancel_label:
        cancel_label = "Cancel"

    def _get_yad_args():
        args = [
            "yad", "--text-info", "--window-icon", window_icon,
            "--title", title, "--width", str(width), "--height", str(height),
            f"--button={ok_label}:0", "--wrap",
            "--margins", "2", "--center"
        ]

        if add_cancel_button:
            args += [f"--button={cancel_label}:1"]

        return args

    def _get_zenity_args():
        args = [
            "zenity", "--text-info", "--window-icon", window_icon,
            "--title", title, "--width", str(width), "--height",
            str(height), "--cancel-label", cancel_label, "--ok-label", ok_label
        ]

        return args"""

new_func = """def show_text_dialog(
        title,
        text,
        window_icon,
        options=None):
    \"\"\"
    Show a text dialog to the user

    :returns: True if user clicked OK, False otherwise
    \"\"\"
    if options is None:
        options = DialogOptions()

    def _get_yad_args():
        args = [
            "yad", "--text-info", "--window-icon", window_icon,
            "--title", title, "--width", str(options.width), "--height", str(options.height),
            f"--button={options.ok_label}:0", "--wrap",
            "--margins", "2", "--center"
        ]

        if options.add_cancel_button:
            args += [f"--button={options.cancel_label}:1"]

        return args

    def _get_zenity_args():
        args = [
            "zenity", "--text-info", "--window-icon", window_icon,
            "--title", title, "--width", str(options.width), "--height",
            str(options.height), "--cancel-label", options.cancel_label, "--ok-label", options.ok_label
        ]

        return args"""

content = content.replace(old_func, new_func)

old_prompt_call = """    if show_dialog:
        ignore = show_text_dialog(
            title="Protontricks",
            text=message,
            window_icon="wine",
            cancel_label="Close",
            ok_label="Ignore, don't ask again",
            add_cancel_button=True
        )"""

new_prompt_call = """    if show_dialog:
        ignore = show_text_dialog(
            title="Protontricks",
            text=message,
            window_icon="wine",
            options=DialogOptions(
                cancel_label="Close",
                ok_label="Ignore, don't ask again",
                add_cancel_button=True
            )
        )"""

content = content.replace(old_prompt_call, new_prompt_call)

with open("src/protontricks/gui.py", "w") as f:
    f.write(content)
