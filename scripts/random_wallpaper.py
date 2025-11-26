import random
import os
from pathlib import Path

directory = f'{Path.cwd()}/.config'
files = os.listdir(f'{directory}/hypr/wallpapers')
files.sort()
with open(f'{directory}/hypr/hyprpaper.conf', 'r') as file:
    current_wallpaper = file.readline()[:-1].split('/')[-1]
random_wallpaper = files[random.randint(0, len(files) - 1)]
files.pop(files.index(current_wallpaper))
with open(f'{directory}/hypr/hyprpaper.conf', 'w') as file:
    file.write(f'preload = {directory}/hypr/wallpapers/{random_wallpaper}\n')
    file.write(f'wallpaper = eDP-1, {directory}/hypr/wallpapers/{random_wallpaper}\n')