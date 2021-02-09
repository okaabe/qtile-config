import os
from typing import List  # noqa: F401

from libqtile import bar, widget
from libqtile.config import (
    Screen,
)
from libqtile.widget.memory import Memory

from bloat.widgets.windowname import WindowName as CustomWindowName

from apps import kill_window, open_launcher, open_powermenu, open_pavu, open_wifimenu, open_notifmenu
from themes.current import colors

terminal = "alacritty"

group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors[4],
    "inactive": colors[10],
    "disable_drag": True,
    "rounded": True,
    "highlight_color": colors[2],
    "block_highlight_text_color": colors[6],
    "highlight_method": "block",
    "this_current_screen_border": colors[14],
    "this_screen_border": colors[7],
    "other_current_screen_border": colors[14],
    "other_screen_border": colors[14],
    "foreground": colors[1],
    "background": colors[14],
    "urgent_border": colors[3],
    "fontsize": 17,
}

bar = bar.Bar(
    [
        # widget.Image(
        #   background=colors[0],
        #    filename="~/.config/qtile/icons/qtilelogo.png",
        #    margin=6,
        #    mouse_callbacks={
        #        "Button1": lambda qtile: qtile.cmd_spawn(
        #            "./.config/rofi/launchers/ribbon/launcher.sh"
        #        )
        #    },
        # ),
        widget.TextBox(
            text="   ",
            foreground=colors[9],
            background=colors[0],
            font="Font Awesome 5 Free Solid",
            fontsize=22,
            # padding=15,
            mouse_callbacks={"Button1": open_launcher},
        ),
        # widget.Sep(
        #    linewidth=2,
        #    foreground=colors[2],
        #    padding=25,
        #    size_percent=50,
        # ),
        widget.TextBox(
            text="",
            foreground=colors[14],
            background=colors[0],
            fontsize=27,
            padding=0,
        ),
        widget.GroupBox(**group_box_settings),
        widget.TextBox(
            text="",
            foreground=colors[14],
            background=colors[0],
            fontsize=27,
            padding=0,
        ),
        widget.Sep(
            linewidth=0,
            foreground=colors[2],
            background=colors[0],
            padding=10,
            size_percent=40,
        ),
        widget.Spacer(),
        # widget.TextBox(
        #     text="",
        #     foreground=colors[14],
        #     background=colors[0],
        #     fontsize=27,
        #     padding=0,
        # ),
        # widget.CurrentLayoutIcon(scale=0.60, background=colors[14]),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            # background=colors[14],
            # padding=-2,
            scale=0.80,
        ),
        CustomWindowName(
            background=colors[0],
            foreground=colors[9],
            width=bar.CALCULATED,
            empty_group_string="Desktop",
            max_chars=25,
            mouse_callbacks={"Button2": kill_window},
        ),
        # widget.TextBox(
        #     text="",
        #     foreground=colors[14],
        #     background=colors[0],
        #     fontsize=27,
        #     padding=0,
        # ),
        widget.Spacer(),
        widget.TextBox(
            text="",
            foreground=colors[14],
            background=colors[0],
            fontsize=27,
            padding=0,
        ),
        widget.Systray(
            icon_size=17,
            padding=10,
            background=colors[14],
        ),
        # widget.TextBox(
        #     text="   ",
        #     background=colors[14],
        # foreground=colors[10],
        # fontsize=17,
        # mouse_callbacks={"Button1": open_powermenu},
        # ),
        widget.TextBox(
            text="",
            foreground=colors[14],
            background=colors[0],
            fontsize=27,
            padding=0,
        ),
        widget.Sep(
            linewidth=2,
            foreground=colors[0],
            padding=10,
            size_percent=50,
        ),
        # widget.TextBox(
        #     text="",
        #     foreground=colors[14],
        #     background=colors[0],
        #     fontsize=27,
        #     padding=0,
        # ),
        # widget.Sep(
        #     linewidth=2,
        #     foreground=colors[3],
        #     background=colors[3],
        #     padding=15,
        #     size_percent=50
        # ),
        # widget.TextBox(
        #     text="",
        #     foreground=colors[3],
        #     background=colors[0],
        #     fontsize=27,
        #     padding=0,
        # ),
        # widget.Sep(
        #     linewidth=2,
        #     foreground=colors[0],
        #     padding=8,
        #     size_percent=50,
        # ),
        widget.Image(
            filename="~/.config/qtile/icons/notification.png",
            mouse_callback={"Button1": open_notifmenu},
            padding=15
        ),
        widget.Sep(
            linewidth=2,
            foreground=colors[0],
            padding=15,
            size_percent=50,
        ),
        # widget.TextBox(
        #     text="",
        #     foreground=colors[4],
        #     font="Font Awesome 5 Free Solid",
        #     fontsize=18,
        #     padding=27,
        #     mouse_callbacks={"Button1": open_powermenu},
        # )
    ],
    24,
    margin=[3, -4, 0, -4]
)
