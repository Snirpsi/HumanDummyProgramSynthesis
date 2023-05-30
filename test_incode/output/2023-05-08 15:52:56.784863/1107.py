#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that enumerates fruits.
    while True:
        fruit = input("Enter a fruit: ")
        if fruit in fruirs:
            print("You chose " + fruit)
        else:
            print("Sorry, I didn't know that fruit.")
            break

