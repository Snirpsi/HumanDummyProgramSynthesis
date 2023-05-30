#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that iterates over fruits.
    while True:
        fruits = input("Enter a fruit or type 'quit' to quit: ")
        if fruits == "quit":
            break
        else:
            fruit = fruits.lower()
            if fruit not in fruirs:
                print("Sorry, that fruit isn't in our list of fruits!")
            else:
                print("You chose " + fruit + "!")

