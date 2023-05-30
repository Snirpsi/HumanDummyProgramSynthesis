#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that stores fruits.
    while True:
        fruit = input("Enter a fruit: ")
        if fruit in fruirs:
            print(fruit)
        else:
            print("That fruit isn't in our list!")

