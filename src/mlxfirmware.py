"""
The following people helped create the code below
Caspian Hedlund, Jimmy Parra, Jordan Hendricks, Tyrone Stagner
File modified on 5/27/2021

Reading the data sheet and looking at some code from adafruit 
that is programmed in C for an arduino and looking at the 
code from a user on github I was able to get this to work 
finally. The git hub web page is
"https://github.com/CRImier/python-MLX90614/blob/master/mlx90614.py"

The data sheet says we are able to acces diffrent registers 
by diffrent hex values to get the data from the MLX 60914. 
We are only going to need to use the hex values 0x07 which 
points to the correct address for getting the tempature. 
We are also able to use the Hex value 0x06 which will display 
the tempature of the sensor or ambiant tempature. 
"""
#we need to import SMBUS to get it to work on the pi
import smbus
#We are going to import time and sleep so we are able to 
#use them int he code when needed. 
import time

#We need to create a class so that we can import it inot 
#the main progrma for the project. 
class MLXSERIES():

#We are creating varibles to have them equal the hex values 
#that we are accessing in the sensor. 
    MLX90614_AMBTEMP=0x06
    MLX90614_TEMP=0x07

    comattempts = 5
#have to make the connection to the smbus  and define the 
#address we are goning to be  reading data from
# has to be __init__ becuase it will throw a constructor error.
    def __init__(self, address=0x5a, busport=1):
        self.busport = busport
        self.address = address
        self.bus = smbus.SMBus(bus=busport)
#This is going to go through and try and make a connection to the 
#register in the device if it can not detet it will throw in error
    def read_reg(self, reg_addr):
        err = None
        for i in range(self.comattempts):
            try:
                return self.bus.read_word_data(self.address, reg_addr)
            except IOError as e:
                err = e
                #"Rate limiting" - sleeping to prevent problems with sensor
                #when requesting data too quickly
                sleep(0.1)
        #By this time, we made a couple requests and the sensor didn't respond
        #(judging by the fact we haven't returned from this function yet)
        #So let's just re-raise the last IOError we got
        raise err
#we need to define the data that we are getting and perform 
#the calculation to get the temp. The 0.02 comes from the 
#data sheet telling us to do this to calculate the correct temp.
    def data_to_temp(self, data):
        temp = (((data*0.02) - 273.15)*(9/5)) + 35
        temp = round(temp,1)
        return temp
#we need to get the data for the AMBTEMP  register and then pass it 
#into the data_to_temp to calculate the tempature
    def get_AMBTEMP(self):
        data = self.read_reg(self.MLX90614_AMBTEMP)
        return self.data_to_temp(data)
#we need to get the data for the TEMP register and then pass it into 
#the data_to_temp to calculate the tempature
    def get_TEMP(self):
        data = self.read_reg(self.MLX90614_TEMP)
        return self.data_to_temp(data)

# this just helps us print the tempature of AMBTEMP and TEMP, we will have to use
# these fuctions in our main program to get the tempatures for them.
if __name__ == "__main__":
    sensor = MLXSERIES()
    print(sensor.get_AMBTEMP())
    print(sensor.get_TEMP())
