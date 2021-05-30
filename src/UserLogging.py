# The following people helped create the code below
# Caspian Hedlund, Jimmy Parra, Jordan Hendricks, Tyrone Stagner
# File modified on 5/27/2021
import csv
from datetime import datetime
import random

# Store the given information into a dynamic array 
def getInfo(rows, UserNum, Temp):
  now = datetime.today()
  a = [now.strftime("%m/%d/%Y %H:%M:%S"), "User Number: "  + str(UserNum),
  str(Temp)]
  rows.append(a)

# Creates the CSV file from the information from the array
def CreateCsv(Legend, rows):
  with open('User_Data', 'a+') as f:

# using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(Legend)
    write.writerows(rows)
