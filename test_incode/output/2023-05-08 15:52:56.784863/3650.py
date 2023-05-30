#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that calculates fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            print("You chose " + fruir)
        else:
            print("Sorry, I do not like " + fruir)
            break

