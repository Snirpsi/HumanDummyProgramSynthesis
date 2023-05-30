#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that stores fruits.
    while True:
        fruir = input("Enter a fruit: ")
        if fruir in fruirs:
            print("You entered a fruit!")
        else:
            print("Sorry, that fruit isn't in the list!")
            break

