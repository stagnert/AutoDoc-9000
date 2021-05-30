# The following people helped create the code below
# Caspian Hedlund, Jimmy Parra, Jordan Hendricks, Tyrone Stagner
# File modified on 5/27/2021

from gpiozero import LED, Button
from signal import pause
from mlxfirmware import MLXSERIES
import time
import os
import ThermometerFunctions
from DisplayFuncs import *
from UserLogging import *


userNum = 1
curTemp = 0
mainLooper = 1
ledg = ['time', 'user', 'temp']
rows = []

MLX_IR_ADD = 0x5a #define I2C register address

#Pass register address back into MLXSERIES class and store read value
therm_data = MLXSERIES(MLX_IR_ADD)

#Main Program
InitDisp() #Initialize the OLED display
while mainLooper == 1:

    # will set gpio alt pins for 13 to make
    # sure speaker will work every time.
    os.system('gpio_alt -p 13 -f 0')

    ReadyDisp() # Will disply when ready

    #loop until input is detected
    while ThermometerFunctions.checkForInput() == False:
        pass #Do nothing until the user wakes the system up
    clearDisp() #clears display
    UserDisp(userNum) #Display current user number
    # will call omxplayer and play wav file
    os.system('omxplayer /home/pi/Documents/Place.wav')
    #Calls ThermometerFunctions and creates a beep
    ThermometerFunctions.beep()

    clearDisp() #Clear Display

    curTemp = therm_data.get_TEMP() #Get temperature

    TempDisp(curTemp) #Display temperature
    time.sleep(4)
    # If power is lost it will restart the user 
    #number to 1, but displays time and date for each user. 
    # you will be able to tell when power is lost 
    #by it reseting the user number to 1. 
    getInfo(rows, userNum, curTemp) #gets info
    CreateCsv(ledg, rows) # Creates the Text dat for CSV file
    userNum = userNum +1 # will increment the user by 1 each time
    
    if float(curTemp) >= 100.4:
        # will set gpio alt pins for 13 to make sure speaker will work every time.
        os.system('gpio_alt -p 13 -f 0') 
        os.system('omxplayer /home/pi/Documents/Fever.wav')

    time.sleep(1) # will sleep for  4 seconds before clearing diplay
    clearDisp() #Turn off display




