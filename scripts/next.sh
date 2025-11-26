var1=1
while  [ $var1 ] 
do
sleep 30
python ~/.config/scripts/next_wallpaper.py 
sleep 1
pkill hyprpaper
hyprpaper 
done
