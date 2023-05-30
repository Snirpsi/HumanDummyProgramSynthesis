#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that iterates over fruits.
    while True:
        print("Enter a fruit: ")
        fruit = input()
        if fruit in fruirs:
            print("The fruit is", fruit)
        else:
            print("The fruit is", fruirs[0])

