
from Game import Warrior_Dice
from Game import SRK_Dice
from Game import Pakola_Dice
from Game import Jojo_Dice

from random import random
from tkinter.messagebox import YES

print("Welcome to KingZone Dragon X")
adventure = input("Would you like to go on a adventure? Yes/No ")  
if adventure == "yes":
    print("Pick your adventure")
    option = input("fighting or Saving?  ")
    if option == "fighting":
        print("You are SubZero a bounty hunter Who's mission is to kill lord JOJO to claim your gold!")
        print (" You excel in Defense Attack and Stamina")
    if option == "saving":
        print("you are now scorpion a banker who lost all his money")
    t = input("Are you ready to earn some money back? YES/NO")
    if t == YES:
        print("GOOD your attributes are Smart, Slick and Manipulative")
    jojo = input("Are you ready to face jojo? Yes/No  ")
    if jojo == YES:
        print("You will first need to beat one of jojo's minions called SRK")
    SRK = input("Are you ready to fight SRK?   Yes/NO  ")
    if SRK == YES:
        print(" You will need to roll a dice first ")
        print( " Depending on the number of the dice is how strong your attack will be")
        print("rolling Dice  ")

    if Warrior_Dice > SRK_Dice:
        print("Warrior wins")
    elif SRK_Dice > Warrior_Dice:
        print("SRK wins")
    else:
        print("It's a draw")

    print("Game Over")


    next = input("Would you like to continue?  Yes/No    ")
    if next == YES:
        print ("Good Job making to the next round!")
    
        print( "Now you're against JOJO'S right hand man called Pakola ")

    a = input("you are now going against Pakola! Are you Ready?  YES/NO  "  )
    if a == YES:
        print(" goodluck!")

    print("warrior rolled: ", Warrior_Dice)
    print("Pakola rolled: ", Pakola_Dice)

    if Warrior_Dice > SRK_Dice:
        print("Warrior wins")
    elif SRK_Dice > Warrior_Dice:
        print("PAKOLA wins")
    else:
        print("It's a draw")

print("Game Over")
j = input("Would you like to continue? Yes/NO  ")
if j == YES:
    print("You are now against the Final BOSS!! JOJO!!!")

c = input(" ARE you ready to go against the Final BOSS JOJO? YES/NO "  )
if c == YES:
    print("GOODLUCK!!")

print("warrior rolled: ", Warrior_Dice)
print("JOJO rolled: ", Jojo_Dice)

if Warrior_Dice > Jojo_Dice:
    print("Warrior wins")
elif Jojo_Dice > Warrior_Dice:
    print("PAKOLA wins")
else:
    print("It's a draw")

print("Game Over")
print("Thank You For Playing")