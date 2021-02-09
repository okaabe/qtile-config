from typing import List  # noqa: F401

from libqtile.config import (
    Key,
    Group,
    ScratchPad,
    DropDown,
)
from libqtile.lazy import lazy

from constants import mod
from binds.keys import keys

workspaces = [
    {
        "name": "",
        "key": "1",
        "matches": []
    },
    {
        "name": "",
        "key": "2",
        "matches": [],
    },
    {
        "name": "",
        "key": "3",
        "matches": [],
    },
    {
        "name": "",
        "key": "4",
        "matches": []
    },
    {
        "name": "ﭮ",
        "key": "5",
        "matches": []
    }
]


groups = [
    ScratchPad(
        "scratchpad",
        [
            # define a drop down terminal.
            # it is placed in the upper third of screen by default.
            DropDown(
                "term",
                "alacritty --class dropdown -e tmux_startup.sh",
                height=0.6,
                on_focus_lost_hide=False,
                opacity=1,
                warp_pointer=False,
            ),
            DropDown(
                "fm",
                "thunar",
                width=0.6,
                height=0.6,
                x=0.2,
                y=0.1,
                on_focus_lost_hide=False,
                opacity=1,
                warp_pointer=True,
            ),
        ],
    ),
]

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout="bsp"))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, "shift"],
            workspace["key"],
            lazy.window.togroup(workspace["name"]),
            desc="Move focused window to another group",
        )
    )
