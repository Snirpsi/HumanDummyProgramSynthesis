#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that stores fruits.
    while True:
        fruits = input("Enter a fruit or type 'quit' to quit: ")
        if fruits == "quit":
            break
        else:
            fruit = fruits.lower()
            fruirs.append(fruit)
    print("Your fruit list is: ", fruirs)

