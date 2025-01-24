#!/usr/bin/env fish
set -x CONFIG_FILE "$HOME/.config/fish/conf.d/nav.fish"
echo "abbr -a -- nav \"source \$HOME/.config/nav/nav\"" >"$CONFIG_FILE"
