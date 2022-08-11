import random
from random import randint

print("Enjoy The Game")

n = input("Enter plyer name : ")
print("Hello "+ n +" Welcome to Number Guessing Game ")

def fun():
    rand_no = randint(1, 10)
    Hint_1 = rand_no / 2;
    Hint_2 = rand_no * 2;
    print("Please select the number between 1 to 10. \nYou have only 3 chances to win the Game")
    i = 1
    lost = 1
    while i<=3:
        number = int(input("Enter the number: "))
        if number <= 1 or number > 10:
            print("\n"+n+"Please Enter a number between 1 to 10 ")
            continue
        elif number < rand_no:
            print("\n"+n+" The Secret Number Is Greater Then your guessed number")
            print("HINT = The Secret number is related to this two number "+str(Hint_1)+", "+str(Hint_2)+"  Please find it")
            print("Now " + str(3 - i) +  " Chances left")
            i = i + 1
        elif number > rand_no:
            print("\n"+n+" The Secret Number Is Smaller Then your guessed number")
            print("HINT = The Secret number is related to this two number "+str(Hint_1)+", "+str(Hint_2)+"  Please find it")
            print("Now " + str(3 - i) + " Chances left")
            i = i + 1
        elif number == rand_no:
            print("\nCongrats " + n + " You Won The Game")
            lost = 0
            break
        else:
            print("This is an invalid number.   please try again")
            print("Now" + str(3 - i) + " Chances left")
            continue
    if lost==1:
        print("Ooops you lost the amazing game!!")
        print("The correct number is "+ str(rand_no))

def main():
    fun()
    while True:
        more = input("Play again to won the game.\nIf you want to play. press 'Y' = ")
        if more == "Y":
            fun()
        else:
            break

main()
print("\nTHANKYOU "+n+" for playing the game!")
