#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that stores fruits.
    while True:
        #Ask the user to input a fruit.
        fruit = input("Enter a fruit: ")
        #If the fruit isn't in the fruirs list, print a message and exit.
        if fruit not in fruirs:
            print("Sorry, that fruit isn't in the fruirs list. Try again.")
            continue
        #If the fruit is in the fruirs list, print a message and exit.
        else:
            print("The fruit is", fruit)
            break

