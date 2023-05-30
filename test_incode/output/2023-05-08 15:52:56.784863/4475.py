#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that prints fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            print("You entered " + fruir)
        else:
            print("Sorry, I didn't know that fruit.")

