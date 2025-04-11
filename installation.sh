#!/usr/bin/env fish
set -x CONFIG_FILE "$HOME/.config/fish/conf.d/nav.fish"
echo "function nav
    source \$HOME/.config/nav/nav
end" >>"$CONFIG_FILE"
