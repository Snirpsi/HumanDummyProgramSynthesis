#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that iterates over fruits.
    while True:
        print("Enter a fruit: ")
        fruit = input()
        if fruit in fruirs:
            print("You found a fruit.")
        else:
            print("Sorry, I didn't find that fruit.")

