print("*************************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return  currentGasLevel


print(gasLevelGauge())