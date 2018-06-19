import collections
import math
from random import SystemRandom
import os
import random
import re
import sys

# Dice roller - n d m
# n = number of dice
# m = how many sides of dice

def rollDice(rolls, sides) :
    randomGen = random.SystemRandom()
    temp = 0
    sum = 0
    outcomes = []
    for x in range(0, rolls) :
        temp = randomGen.randint(1, sides)
        outcomes.append(temp)
        sum += temp
    outcomes.append(sum)
    return (outcomes)
    


for i in range(1, len(sys.argv)) : 
    roll = sys.argv[i].split('d')
    currRoll = rollDice(int(roll[0]), int(roll[1]))

    # Print the Sum of all rolls and a semi-colon
    print("\n%d: " % (currRoll[len(currRoll)-1]), end ='')

    # Print each individual roll
    for y in range(0, len(currRoll)-1) :
        print("%d " % (currRoll[y]),end = '')

