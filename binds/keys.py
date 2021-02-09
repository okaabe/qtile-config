# -*- coding: utf-8 -*-
from libqtile.config import (
    Key,
)
from libqtile.lazy import lazy

from constants import mod, terminal


def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                    direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                    direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    resize(qtile, "left")


@lazy.function
def resize_right(qtile):
    resize(qtile, "right")


@lazy.function
def resize_up(qtile):
    resize(qtile, "up")


@lazy.function
def resize_down(qtile):
    resize(qtile, "down")


keys = [
    Key(["shift"], "Left", lazy.screen.prev_group()),
    Key(["shift"], "Right", lazy.screen.next_group()),
    #Key([mod, "shift"]),
    ### The essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launches My Terminal"),
    Key(
        [mod],
        "e",
        lazy.spawn("./.config/rofi/launchers/colorful/launcher.sh"),
        # lazy.spawn("rofi -display-drun '' -show drun -drun-show-actions"),
        desc="Rofi app launcher",
    ),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle through layouts"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill active window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key(
        [mod, "shift"],
        "e",
        lazy.spawn("./.config/rofi/powermenu/powermenu.sh"),
        desc="Power Menu",
    ),
    Key(
        [mod, "shift"],
        "a",
        lazy.spawn("code /home/okaabe/.config/qtile/config.py"),
        desc="Config qtile",
    ),
    ### Window controls
    Key(
        [mod], "Down", lazy.layout.down(), desc="Move focus down in current stack pane"
    ),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod],
        "Left",
        lazy.layout.left(),
        lazy.layout.next(),
        desc="Move focus left in current stack pane",
    ),
    Key(
        [mod],
        "Right",
        lazy.layout.right(),
        lazy.layout.previous(),
        desc="Move focus right in current stack pane",
    ),
    Key(
        [mod, "shift"],
        "Down",
        lazy.layout.shuffle_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "Up",
        lazy.layout.shuffle_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        lazy.layout.swap_left(),
        lazy.layout.client_to_previous(),
        desc="Move windows left in current stack",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right(),
        lazy.layout.client_to_next(),
        desc="Move windows right in the current stack",
    ),
    Key([mod, "control"], "Down", lazy.layout.flip_down(), desc="Flip layout down"),
    Key([mod, "control"], "Up", lazy.layout.flip_up(), desc="Flip layout up"),
    Key([mod, "control"], "Left", lazy.layout.flip_left(), desc="Flip layout left"),
    Key([mod, "control"], "Right", lazy.layout.flip_right(), desc="Flip layout right"),
    Key(
        [mod, "mod1"],
        "Left",
        resize_left,
        desc="Resize window left",
    ),
    Key(
        [mod, "mod1"],
        "Right",
        resize_right,
        desc="Resize window Right",
    ),
    Key([mod, "mod1"], "Up", resize_up, desc="Resize windows upward"),
    Key([mod, "mod1"], "Down", resize_down, desc="Resize windows downward"),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "equal", lazy.layout.grow(), desc="Grow in monad tall"),
    Key([mod], "minus", lazy.layout.shrink(), desc="Shrink in monad tall"),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on focused window",
    ),
    ### Stack controls
    Key(
        [mod],
        "f",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies {MonadTall}",
    ),
    # Key(
    #    [mod],
    #    "f",
    #    lazy.layout.next(),
    #    desc="Switch window focus to other pane/s of stack",
    # ),
    Key(
        [mod],
        "s",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    ### Misc. Commands
    Key(
        [mod],
        "b",
        lazy.spawn("qtile-cmd -o cmd -f hide_show_bar"),
        desc="Toggle bar visibility",
    ),
    Key(
        [mod],
        "backslash",
        lazy.spawn("sh -c 'thunar \"$(xcwd)\"'"),
        desc="Launch thunar",
    ),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn("./.config/qtile/scripts/focus_mode.sh"),
        desc="Toggle focus mode",
    ),
    Key(
        ["control"],
        "Tab",
        lazy.spawn("rofi -theme ~/.config/rofi/configWindow.rasi -show window"),
        # lazy.spawn("rofi -display-window '□' -show window"),
        desc="Rofi window select",
    ),
    Key(
        [],
        "Print",
        lazy.spawn("flameshot gui"),
        desc="Print Screen",
    ),
    Key(
        [mod],
        "z",
        lazy.spawn("./.config/sxhkd/old_scripts/rofi-files"),
        desc="Find files",
    ),
    Key(
        [mod, "control"],
        "n",
        lazy.spawn("./.config/sxhkd/old_scripts/toggledunst"),
        desc="Toggle dunst",
    ),
    Key(
        [mod],
        "n",
        lazy.spawn("./.local/bin/rofi_notif_center.sh"),
        desc="Open notification center",
    ),

    Key(
        ["mod1", "shift"],
        "1",
        lazy.spawn("./.config/rofi/applets/android/volume.sh")
    ),
    Key(
        ["mod1", "shift"],
        "2",
        lazy.spawn("./.config/rofi/applets/android/quicklinks.sh")
    ),
    Key(
        ["mod1", "shift"],
        "3",
        lazy.spawn("./.config/rofi/applets/applets/network.sh")
    ),
]


def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<30} {}".format(mods, k.desc + "\n")

    return key_help


keys.extend(
    [
        Key(
            [mod],
            "a",
            lazy.spawn(
                "sh -c 'echo \""
                + show_keys()
                + '" | rofi -dmenu -theme ~/.config/rofi/configTall.rasi -i -p "?"\''
            ),
            desc="Print keyboard bindings",
        ),
    ]
)
