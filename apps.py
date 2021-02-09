from typing import List  # noqa: F401
from libqtile import qtile

from constants import terminal


def open_launcher():
    qtile.cmd_spawn("./.config/rofi/launchers/ribbon/launcher.sh")


def finish_task():
    qtile.cmd_spawn('task "$((`cat /tmp/tw_polybar_id`))" done')


def kill_window():
    qtile.cmd_spawn("xdotool getwindowfocus windowkill")


def update():
    qtile.cmd_spawn(terminal + "-e yay")


def open_pavu():
    qtile.cmd_spawn("pavucontrol")


def toggle_bluetooth():
    qtile.cmd_spawn("./.config/qtile/scripts/system-bluetooth-bluetoothctl.sh --toggle")


def open_bt_menu():
    qtile.cmd_spawn("blueman")


def open_connman():
    qtile.cmd_spawn("connman-gtk")


def todays_date():
    qtile.cmd_spawn("./.config/qtile/scripts/calendar.sh")


def open_powermenu():
    qtile.cmd_spawn("./.config/rofi/powermenu/powermenu.sh")


def open_window_switcher():
    qtile.cmd_spawn("./.config")


def open_volumemenu():
    qtile.cmd_spawn("./.config/rofi/applets/android/volume.sh")


def open_wifimenu():
    qtile.cmd_spawn("./.config/rofi/applets/applets/network.sh")


def open_notifmenu():
    qtile.cmd_spawn("./.local/bin/rofi_notif_center.sh")
