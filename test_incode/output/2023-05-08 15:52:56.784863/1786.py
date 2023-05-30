#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that enumerates fruits.
    while True:
        print("\nFruit enumeration")
        for fruit in fruirs:
            print(fruit)
        print("\nPress enter to continue")
        line = input()

