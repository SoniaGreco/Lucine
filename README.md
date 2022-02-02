# Lucine
A slider GUI to change brightness of the screen. It is compatible with Dell XPS 7590.

# Requirements
Install tkinter library
`sudo apt-get install python3-tk`

# Usage
- Put lucine_slider.desktop file in ~/.local/share/applications.
- In lucine_slider.desktop file update the paths of lucine.py and lucine.png with your actual path
- Give executable rights to both lucine.py and lucine_slider.desktop files with
  `chmod -x lucine.py` `chmod -x lucine_slider.desktop`
- Open a terminal in the folder containing lucine.py and run `python3 lucine.py`
- if you encounter problems with eDP-1, type in a terminal `xrandr --listactivemonitors` and replace eDP-1 with whatever is in the output, e.g. eDP-1-1.


# Icon
Optional: add the icon to Favorites for easy launch!


![](lucine_bassa.png)


# View
![](lucine_view.png)
