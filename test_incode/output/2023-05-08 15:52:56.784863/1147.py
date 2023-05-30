#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        print("Add fruits:")
        for fruit in fruirs:
            print("\t" + fruit)
        choice = input("\nChoose a fruit: ")
        if choice in fruirs:
            fruirs.remove(choice)
        else:
            print("That fruit isn't in the list!")

