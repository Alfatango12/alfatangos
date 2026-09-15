# Grant access to GTK CSS configs (covers both GTK3 and GTK4/Libadwaita user stylesheets)
flatpak override --user --filesystem=xdg-config/gtk-3.0:ro
flatpak override --user --filesystem=xdg-config/gtk-4.0:ro

# Grant access to local themes and icons folders
flatpak override --user --filesystem=xdg-data/themes:ro
flatpak override --user --filesystem=xdg-data/icons:ro
flatpak override --user --filesystem=~/.themes:ro
flatpak override --user --filesystem=~/.icons:ro
# QT themes
flatpak override --user --filesystem=xdg-config/qt6ct:ro
flatpak override --user --env=QT_QPA_PLATFORMTHEME=qt6ct
flatpak override --user --filesystem=xdg-data/color-schemes:ro
cp ~/.config/qt6ct/colors/"dank shell.colors" ~/.local/share/color-schemes/
ln -sf ~/.config/qt6ct/colors/"dank shell.colors" ~/.local/share/color-schemes/
ln -sf "../../../.config/qt6ct/colors/dank shell.colors" ~/.local/share/color-schemes/"dank shell.colors"
flatpak override --user --filesystem=xdg-config/kdeglobals:ro
