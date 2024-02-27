print("\n************************************************************\n")

print("Weather Branch\n")

#Import Libraries here
import random
from time import sleep

#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["snowing","blizzard","raining","foggy","windy","icy","sunny"]
    weatherCondtions = random.choice(weatherForecast)
    return weatherCondtions

# Variable tocall the weather() once VRS (Vehicale Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\nNational Weather Service has updated our alarm by 30 minutes becasuse of the forecast of",weatherAlert,
        "Weather conditions.")
        print("VRS has been engaged only allowing you to drive 50mph.")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes becasuse of the forecast of", weatherAlert,
              "Weather conditions.")
        print("VRS has been engaged only allowing you to drive 40mph.")
    elif weatherAlert == "raining":
        print("\nNational Weather Service has updated our alarm by 10 minutes becasuse of the forecast of", weatherAlert,
              "Weather conditions.")
        print("VRS has been engaged only allowing you to drive 60mph.")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 10 minutes becasuse of the forecast of", weatherAlert,
              "Weather conditions.")
        print("VRS has been engaged only allowing you to drive 60mph.")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 10 minutes becasuse of the forecast of", weatherAlert,
              "Weather conditions.")
        print("VRS has been engaged only allowing you to drive 70mph.")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes becasuse of the forecast of", weatherAlert,
              "Weather conditions.")
        print("VRS has been engaged only allowing you to drive 30mph.")
    else:
        print("\nNational Weather Service has a forecast of", weatherAlert,
              "Weather conditions.")
        print("VRS has been disengaged have a nice day.")



vehicleResponseSystem()
