#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that converts fruits.
    while True:
        fruits = input("Enter a fruit: ")
        if fruits == "quit":
            break
        else:
            fruits = fruits.lower()
            fruits = fruits.split()
            for fruit in fruits:
                if fruit not in fruirs:
                    print(fruit)

