from bloat.layout import layouts, layout_theme, floating_layout

from bloat.screens import screens
from bloat.groups import groups

from binds.keys import keys
from binds.mouse import mouse

from autostart import (
    start_once,
    _swallow,
    _unswallow,
    modify_window
)


from themes.current import colors

mod = "mod4"
terminal = "alacritty"
widget_defaults = dict(font="FiraCode Nerd Font", fontsize=14, padding=3, background=colors[0])
extension_defaults = widget_defaults.copy()
dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus"

wmname = "LG3D"
