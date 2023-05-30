#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that stores fruits.
    while True:
        fruits = input("Enter a fruit or type 'quit' to quit (type 'quit' to quit): ")
        if fruits == "quit":
            break
        else:
            fruit = fruits.lower()
            if fruit not in fruirs:
                print("That fruit isn't in our list of fruits. Try again.")
            else:
                print("That fruit is in our list of fruits. Good job!")

