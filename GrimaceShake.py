print("*************************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random
from time import sleep 

#Function that lists Gas Levels, randomly choosing one and returing its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Three Quarter Tank","Full Tank"]
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

    

gasLevelAlert()
