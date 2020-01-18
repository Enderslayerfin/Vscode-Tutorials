#Imports
import random
from os import system, name
from time import sleep

#define Clear()
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#sub main code:
first = random.randint(1,12)
second = random.randint(1,26)
third = random.randint(1,26)