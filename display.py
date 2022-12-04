#!/usr/bin/python
# -*- coding:utf-8 -*-

# 360 x 240 display dimensions
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pic")
print(picdir)

import logging
from waveshare_epd import epd3in52
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from datetime import datetime as dt
from enum import Enum
logging.basicConfig(level=logging.DEBUG)

# Upper and lower bouds can be used to create margins easily
class Screen(Enum):
    width = 360
    width_upper = width - 5
    width_lower = 5
    width_center = (width_upper - width_lower) /2
    height = 240
    height_upper = height - 5
    height_lower = 0

try: 
    logging.info("epd3in52 Demo")
    
    epd = epd3in52.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.display_NUM(epd.WHITE)
    epd.lut_GC()
    epd.refresh()

    epd.send_command(0x50)
    epd.send_data(0x17)
    time.sleep(2)
    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
    font12 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)

    # Setting up the image screen
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)

    # Text going within the header of the screen
    draw.text((10, 0), 'home.net', font = font24, fill = 0)
    dttime = dt.now().time()
    dttime = dttime.strftime("%H:%M")
    print(dttime)
    draw.text((300, 0), dttime, font = font24, fill = 0)
    draw.line([(0, 27), (356, 27)], width=1)

    # Box row 1
    draw.text((Screen.width_lower.value, 30), 'Service Status:', font = font18, fill = 0)
    draw.rectangle([(Screen.width_lower.value, 60), (Screen.width_center.value -2, 100)], width=2)
    draw.text((Screen.width_lower.value + 3, 63), "piHole", font=font18, fill=0)
    draw.text((Screen.width_lower.value + 3, 85), "192.168.1.4", font=font12, fill=0)
    draw.text((Screen.width_center.value - 2 - 35, 70), "OFF", font=font18, fill=0)
    draw.rectangle([(Screen.width_center.value + 2, 60), (Screen.width_upper.value, 100)], width=2)
    draw.text((Screen.width_center.value + 5, 63), "Homer", font=font18, fill=0)
    draw.text((Screen.width_center.value + 5, 85), "192.168.1.4", font=font12, fill=0)
    draw.text((Screen.width_upper.value - 2 - 35, 70), "OFF", font=font18, fill=0)

    # Box row 2
    draw.rectangle([(Screen.width_lower.value, 104), (Screen.width_center.value -2, 144)], width=2)
    draw.text((Screen.width_lower.value + 3, 107), "Portainer", font=font18, fill=0)
    draw.text((Screen.width_lower.value + 3, 129), "192.168.1.4", font=font12, fill=0)
    draw.text((Screen.width_center.value - 2 - 35, 114), "OFF", font=font18, fill=0)
    draw.rectangle([(Screen.width_center.value + 2, 104), (Screen.width_upper.value, 144)], width=2)
    draw.text((Screen.width_center.value + 5, 107), "Prometheus", font=font18, fill=0)
    draw.text((Screen.width_center.value + 5, 129), "192.168.1.4", font=font12, fill=0)
    draw.text((Screen.width_upper.value - 2 - 35, 114), "OFF", font=font18, fill=0)

    # Display the created image
    epd.display(epd.getbuffer(Himage))
    epd.lut_GC()
    epd.refresh()

    # The clear command will be required if storing the screen so don't delete it
    # epd.Clear()

    # Sleeping the screen is required so that high voltage dammage is not caused
    epd.sleep()

# Error handling
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd3in52.epdconfig.module_exit()
    exit()
