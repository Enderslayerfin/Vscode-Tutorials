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

clear()
print(" ")
print(" ")

#Main code
#Part 1
if first == 1:
  part1 = "Fuck off"
if first == 2:
  part1 = "Shut the fuck up"
if first == 3:  
  part1 = "Piss off"
if first == 4:
  part1 = "Get out"
if first == 5:
  part1 = "It's RAWWW"
if first == 6:
  part1 = "It's BURNT"
if first == 7:
  part1 = "What the FUCK are you doing"
if first == 8:      
  part1 = "Move your ass"
if first == 9:
  part1 = "More SAUCE"
if first == 10:
  part1 = "Wake up"                   
if first == 11:
  part1 = "Get a grip"
if first == 12:
  part1 = "Gimme your jacket"


#Part 2
if second == 1:
  part2 = "you stupid"
if second == 2:
  part2 = "you lazy"
if second == 3:
  part2 = "you pathetic"
if second == 4:
  part2 = "you useless"
if second == 5:
  part2 = "you silly"
if second == 6:
  part2 = "you ignorant"
if second == 7:
  part2 = "you fat"
if second == 8:
  part2 == "you dumb"
if second == 9:
  part2 = "you little"
if second == 10:
  part2 = "you fucking"
if second == 11:
  part2 = "you bloody"
if second == 12:
  part2 = "you ugly"
if second == 13:
  part2 = "you weird"
if second == 14:
  part2 = "you hopeless"
if second == 15:
  part2 = "you wimpy"
if second == 16:
  part2 = "you goddamn"
if second == 17:
  part2 = "you brainless"
if second == 18:
  part2 = "you slow"
if second == 19:
  part2 = "you proud"
if second == 20:
  part2 = "you fat-mouthed"
if second == 21:
  part2 = "you blasted"
if second == 22:
  part2 = "you wasted"
if second == 23:
  part2 = "you dopey"
if second == 24:
  part2 = "you right"
if second == 25:
  part2 = "you worthless"
if second == 26:
  part2 = "you stinky"


#Part3
if third == 1:
  part3 = "piece of shit"
if third == 2:
  part3 = "asshole"
if third == 3:
  part3 = "donut"
if third == 4:
  part3 = "idiot"
if third == 5:
  part3 = "jerk"
if third == 6:
  part3 = "pig"
if third == 7:
  part3 = "donkey"
if third == 8:
  part3 = "fuckface"
if third == 9:
  part3 = "wanker"
if third == 10:
  part3 = "cow"
if third == 11:
  part3 = "dumbo"
if third == 12:
  part3 = "imbecile"
if third == 13:
  part3 = "bitch"
if third == 14:
  part3 = "muppet"
if third == 15:
  part3 = "banana"
if third == 16:
  part3 = "dickface"
if third == 17:
  part3 = "gremlin"
if third == 18:
  part3 = "bozo"
if third == 19:
  part3 = "fucker"
if third == 20:
  part3 = "fatass"
if third == 21:
  part3 = "dog"
if third == 22:
  part3 = "plank"
if third == 23:
  part3 = "dick"
if third == 24:
  part3 = "giraffe"
if third == 25:
  part3 = "tosser"
if third == 26:
  part3 = "crybaby"

input = input("Press 1 to be insulted by Gordon Ramsey!")
if input == "1":
    print(part1 + " " + part2 + " " + part3 + "!")
else:
    print("You have avoided Gordon this time.")