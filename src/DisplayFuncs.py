# The following people helped create the code below
# Caspian Hedlund, Jimmy Parra, Jordan Hendricks, Tyrone Stagner
# File modified on 5/27/2021

import time
import subprocess

# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create i2c interface
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and 
# pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("DejaVuSans.ttf", 12)

# Initilize the display
def InitDisp():
  # Draw a black filled box to clear the image.
  draw.rectangle((0, 0, width, height), outline=0, fill=0)

  # Draw some shapes.
  # First define some constants to 
  # allow easy resizing of shapes.
  padding = -2
  top = padding
  bottom = height - padding


  draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Clear the display
def clearDisp():
  disp.fill(0)
  disp.show()
  draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Display the current temperature and if a fever was detected
def TempDisp(curTemp):
  draw.text((0, 0), "   Temperature: \n" + str(curTemp), 
  font=font, fill=255, align = "center")
  disp.image(image)
  disp.show()
  time.sleep(3)
  clearDisp()
  if curTemp >= 100.4:
    draw.text((0, 20), "You have a fever!! \n", 
    font=font, fill=255, align = "center")
  disp.image(image)
  disp.show()

# Display the current user number
def UserDisp(UserNum):
  draw.text((0, 0), " User Number: \n " + str(UserNum),
  font=font, fill=255, align = "center")
  disp.image(image)
  disp.show()
# Display when ready to take temp
def ReadyDisp():
  draw.text((0, 0), " Ready \n " +"to take temp " , 
  font=font, fill=255, align = "center")
  disp.image(image)
  disp.show()










