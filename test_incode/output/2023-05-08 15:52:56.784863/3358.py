#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that adds fruits.
    while True:
        fruir = input("Enter a fruit name: ")
        if fruir in fruirs:
            print(fruir + " is a fruit!")
        else:
            print("Sorry, " + fruir + " is not a fruit!")
            break

