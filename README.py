# games
code behind some  games
"""SNAKE,WATER AND GUN GAME"""

import random

print("Welcome to snake water and gun game")
computer = random.randint(-1,1)
compDict = {
    1 : "S",
    -1 : "W",
    0 : "G",
}
youstr = input("Enter your choice between s,w,g: ").upper()
youDict = {
    "S" : 1,
    "W" : -1,
    "G" : 0,
}

you = youDict[youstr]
comp = compDict[computer]
if (computer == you):
    print("draw")
else:    
    if (computer == -1 and you == 1):
        print("you win")
    elif(computer == -1 and you == 0):
        print("you lose")
    elif(computer == 1 and you == -1):
        print("you lose")
    elif(computer == 1 and you == 0):
        print("you win")
    elif(computer == 0 and you == -1):   
        print("you win")
    elif(computer == 1 and you == 0):
        print("you lose") 
    else:
        print("something went wrong")   


print("your choice",youstr,"computer choice is",comp)
