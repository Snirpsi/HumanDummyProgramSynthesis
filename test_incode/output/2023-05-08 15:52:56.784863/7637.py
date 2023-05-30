#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        fruits = input("Enter a fruit name: ")
        if fruits not in fruirs:
            print("Sorry, that fruit isn't in the list!")
        else:
            fruirs.append(fruits)
            break

