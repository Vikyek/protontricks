import sys
from pathlib import Path

from protontricks.cli.desktop_install import cli, install_desktop_entries


def test_install_desktop_entries(tmp_path, monkeypatch, command_mock):
    """
    Ensure that `install_desktop_entries` copies files to the expected
    directory and executes `desktop-file-install` properly
    """
    monkeypatch.setattr(Path, "home", lambda: tmp_path)

    applications_dir = install_desktop_entries()

    assert applications_dir == tmp_path / ".local" / "share" / "applications"
    assert applications_dir.exists()

    command = command_mock.commands[0]
    assert command.args[0:3] == [
        "desktop-file-install",
        "--dir",
        str(applications_dir)
    ]
    assert command.args[3].endswith("/protontricks.desktop")
    assert command.args[4].endswith("/protontricks-launch.desktop")


def test_cli_no_args(home_dir, command_mock, monkeypatch):
    """
    Ensure `cli()` defaults to using `sys.argv[1:]` when `args` is None
    """
    monkeypatch.setattr(sys, "argv", ["protontricks-desktop-install"])

    cli()

    command = command_mock.commands[0]
    assert command.args[0:3] == [
        "desktop-file-install",
        "--dir",
        str(home_dir / ".local" / "share" / "applications")
    ]


def test_run_desktop_install(home_dir, command_mock, desktop_install_cli):
    """
    Ensure that `desktop-file-install` is called properly
    """
    # `protontricks-desktop-install` takes no arguments
    desktop_install_cli([])

    command = command_mock.commands[0]
    assert command.args[0:3] == [
        "desktop-file-install",
        "--dir",
        str(home_dir / ".local" / "share" / "applications")
    ]
    assert command.args[3].endswith("/protontricks.desktop")
    assert command.args[4].endswith("/protontricks-launch.desktop")
