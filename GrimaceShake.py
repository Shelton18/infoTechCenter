
#Import Libraries Here
import time
import sys
import random
from time import sleep


#Welcome Branch starts here
timeToSleep = 1

print("\n\nWelcome to InforTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsi add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("Infotech Center System Booting"+"."* ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r"+ message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating system Booted Up - Retina Scanned - Access Granted!")



#Gasoline Branch starts here
print("*************************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here


#Function that lists Gas Levels, randomly choosing one and returing its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return  currentGasLevel

# Function that lists Gas Stations,m randomly choosing one and returning its value
def listOfStations():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Moble","Costco","Meijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#Function will call the gasLevelGauge to determin our gas level and then find a close gas station
#by calling the listOfGasStation function if we are on Low or Quarter Tank

def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator== "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2.25)
        print("   ***Calling Triple AAA***")
    elif gasLevelIndicator== "Low": 
        print("Your gas tank is extermly low, cheking Google Maps for the closets gas station...")
        sleep(2.25)
        print("The closest gas station is",listOfStations(),"which is",milesToGasStationsLow,"Miles away.")
    elif gasLevelIndicator== "Quarter Tank": 
        print("Your gas tank is on a quarter Tank, cheking Google Maps for the closets gas station...")
        sleep(2.25)
        print("The closest gas station is",listOfStations(),"which is",milesToGasStationsQuarterTank,"Miles away.")        
    elif gasLevelIndicator== "Half Tank":
        print("Your gas tank is a half of a tank full which is is plenty to get to your destination.")
    elif gasLevelIndicator== "Three Quarter tank": 
        print("your gas tank is at three quarter tank.")
    else:
        print("Gas Tank is Full.")
    
    

gasLevelAlert()
 
