import os
from typing import List  # noqa: F401

from libqtile import bar, widget
from libqtile.config import (
    Screen,
)
from libqtile.widget.memory import Memory

from bloat.widgets.windowname import WindowName as CustomWindowName

from apps import kill_window, open_launcher, open_powermenu, open_pavu, open_wifimenu

from themes.current import colors

terminal = "alacritty"

group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors[9],
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
}

bar = bar.Bar(
    [
        widget.TextBox(
            text="",
            foreground=colors[13],
            background=colors[0],
            font="Font Awesome 5 Free Solid",
            fontsize=20,
            padding=27,
            mouse_callbacks={"Button1": open_launcher},
        ),
        widget.TextBox(
            text="",
            foreground=colors[14],
            background=colors[0],
            fontsize=27,
            padding=0,
        ),
        widget.GroupBox(
            font="Font Awesome 5 Brands",
            visible_groups=["一"],
            **group_box_settings,
        ),
        widget.GroupBox(
            font="Font Awesome 5 Free Solid",
            visible_groups=["二", "三", "四", "五", "六"],
            **group_box_settings,
        ),
        widget.GroupBox(
            font="Font Awesome 5 Brands",
            visible_groups=["七"],
            **group_box_settings,
        ),
        widget.GroupBox(
            font="Font Awesome 5 Free Solid",
            visible_groups=["八", "九", "零"],
            **group_box_settings,
        ),
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
        # widget.TextBox(
        #    text=" ",
        #    foreground=colors[7],
        #    background=colors[0],
        #    font="Font Awesome 5 Free Solid",
        # ),
        # widget.CurrentLayout(
        #    background=colors[0],
        #    foreground=colors[7],
        # ),
        widget.TextBox(
            text="",
            foreground=colors[14],
            background=colors[0],
            fontsize=27,
            padding=0,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            background=colors[14],
            padding=-2,
            scale=0.70,
        ),
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
            padding=10,
            size_percent=50,
        ),
        CustomWindowName(
            background=colors[0],
            foreground=colors[9],
            width=bar.CALCULATED,
            empty_group_string="Desktop",
            max_chars=25,
            mouse_callbacks={"Button2": kill_window},
        ),
        widget.Spacer(),
        widget.Systray(icon_size=20, padding=10),
        widget.TextBox(
            text="   ",
            foreground=colors[9],
            font="Font Awesome 5 Free Solid",
            mouse_callbacks={"Button1": open_wifimenu},
        ),
        widget.Sep(
            linewidth=0,
            foreground=colors[2],
            padding=10,
            size_percent=50,
        ),
        widget.TextBox(
            text="",
            foreground=colors[14],
            background=colors[0],
            fontsize=27,
            padding=0,
        ),
        widget.TextBox(
            text=" ",
            foreground=colors[3],
            background=colors[14],
            font="Font Awesome 5 Free Solid",
            # fontsize=38,
        ),
        widget.memory.Memory(
            background=colors[14],
            foreground=colors[3],
            padding=10,
            format="{MemUsed} M"
        ),
        widget.Sep(
            background=colors[14],
            linewidth=0,
            foreground=colors[2],
            padding=10,
            size_percent=50,
        ),
        widget.TextBox(
            text=" ",
            foreground=colors[8],
            background=colors[14],
            font="Font Awesome 5 Free Solid",
            # fontsize=38,
        ),
        widget.PulseVolume(
            foreground=colors[8],
            background=colors[14],
            limit_max_volume="True",
            mouse_callbacks={"Button3": open_pavu},
        ),
        widget.Sep(
            background=colors[14],
            linewidth=0,
            foreground=colors[2],
            padding=10,
            size_percent=50,
        ),
        widget.TextBox(
            text=" ",
            font="Font Awesome 5 Free Solid",
            foreground=colors[5],  # fontsize=38
            background=colors[14],
        ),
        widget.Clock(
            format="%a, %b %d",
            background=colors[14],
            foreground=colors[5],
        ),
        widget.Sep(
            background=colors[14],
            linewidth=0,
            foreground=colors[2],
            padding=10,
            size_percent=50,
        ),
        widget.TextBox(
            text=" ",
            font="Font Awesome 5 Free Solid",
            foreground=colors[4],  # fontsize=38
            background=colors[14],
        ),
        widget.Clock(
            format="%I:%M %p",
            foreground=colors[4],
            background=colors[14],
            # mouse_callbacks={"Button1": todays_date},
        ),
        widget.TextBox(
            text="",
            foreground=colors[14],
            background=colors[0],
            fontsize=27,
            padding=0,
        ),
        # widget.Sep(
        #    linewidth=2,
        #    foreground=colors[2],
        #    padding=25,
        #    size_percent=50,
        # ),
        widget.TextBox(
            text="⏻",
            foreground=colors[13],
            font="Font Awesome 5 Free Solid",
            fontsize=20,
            padding=27,
            mouse_callbacks={"Button1": open_powermenu},
        )
    ],
    26,
    margin=[0, -4, 0, -4]
)
