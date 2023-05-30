#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that enumerates fruits.
    while True:
        fruits = fruirs
        fruirs = input("Enter a fruit or enter 'q' to quit: ")
        if fruits == "q":
            break
        else:
            fruits = fruirs.split()
            print(fruits)

