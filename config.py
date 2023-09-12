from my_animation import *

RESOLUTION = 1080
# Define your rendering configuration options
RENDER_CONFIG = {
    "pixel_height": RESOLUTION,
    "pixel_width": RESOLUTION * 16//9,
    "progress_bars": "leave",
    "verbose": "WARNING",
    "frame_rate": 60,
   
    "preview": False,
   
 }

with tempconfig(RENDER_CONFIG):
    SCENE_.render()
