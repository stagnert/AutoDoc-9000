# The following people helped create the code below
# Caspian Hedlund, Jimmy Parra, Jordan Hendricks, Tyrone Stagner
# File modified on 5/27/2021

from gpiozero import LED, Button, TonalBuzzer
from gpiozero.tones import Tone
import time


#Functions

def checkForInput():
    btn = Button(17)
    btn.wait_for_press()
    time.sleep(1)
    return True

def wakeUp():
    displayUser
    

def displayUser(userNum):
    print("Patient #"+ str(userNum))
    
def getTemp():
    return input('Enter Temp (for testing)')

def displayTemp(curTemp):
    print(str(curTemp))
    
def displayOff():
    print("Display Off (test)")
    
#Beep once
def beep():
    speaker = TonalBuzzer(13) #Set up speaker GPIO pin
     #Beep a 550 Hz tone
    speaker.play(Tone(550))
    time.sleep(0.25) 
    speaker.stop
    
    
#Beep 3 times 
def beepX3():
    beep()
    time.sleep(0.50)
    beep()
    time.sleep(0.50)
    beep()
    time.sleep(0.50)
def storeData(userNum, curTemp):    
    print("Patient #" + str(userNum) + ", Temp:" + str(curTemp))
