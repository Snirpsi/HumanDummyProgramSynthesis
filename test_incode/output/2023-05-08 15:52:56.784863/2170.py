#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that stores fruits.
    while True:
        fruits = input("Enter a fruit or type 'quit' to quit or type 'exit' to exit: ")
        if fruits == "quit":
            break
        elif fruits == "exit":
            break
        else:
            fruit = fruits.lower()
            if fruit not in fruirs:
                print("Sorry, that fruit isn't in the list!")
            else:
                print("That fruit is in the list!")

