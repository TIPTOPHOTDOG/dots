import os
from pathlib import Path

directory = f'{Path.cwd()}/.config'
files = os.listdir(f'{directory}/hypr/wallpapers')
files.sort()
with open(f'{directory}/hypr/hyprpaper.conf', 'r') as file:
    current_wallpaper = file.readline()[:-1].split('/')[-1]
next_wallpaper = files[files.index(current_wallpaper) + 1 if (files.index(current_wallpaper) + 1 ) < len(files) else 0]
with open(f'{directory}/hypr/hyprpaper.conf', 'w') as file:
    file.write(f'preload = {directory}/hypr/wallpapers/{next_wallpaper}\n')
    file.write(f'wallpaper = eDP-1, {directory}/hypr/wallpapers/{next_wallpaper}\n')