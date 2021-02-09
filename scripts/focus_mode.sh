#!/usr/bin/env bash
#set -euo pipefail

if pgrep conky; then
    pkill conky
    eww open border &
    eww open border1 &
    qtile cmd-obj -o cmd -f hide_show_bar --args top
else
    eww close-all
    qtile cmd-obj -o cmd -f hide_show_bar --args top
fi