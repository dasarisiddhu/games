# games
code behind some  games
"""(1)SNAKE,WATER AND GUN GAME"""

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

"""(2)Number geussing game"""

import random
g = random.randint(1,10)
while True:
    n = int(input("Guess a number between 1 to 10: "))
    if n == g:
        print("✅ You are right!")
        break
    else:
        print("❌ Wrong! Try again.")

"""(3)Number geussing game 2"""
import random
g = random.randint(1,100)
attempts = 0 
while attempts <8:
    n = int(input("Guess a number between 1 to 100: "))
    attempts +=1
    if(n==g):
        print("✅ You are right,you took",attempts,"attempts")
        break
    elif(n > g):
        print("too high")
    elif(n<g):
        print("too low ")

if(attempts == 8 and n!=g):
    print("Game Over! The correct number was", g)




