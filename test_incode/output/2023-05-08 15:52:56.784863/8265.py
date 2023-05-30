#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that requests fruits.
    while True:
        print("\nEnter a fruit: ")
        fruir = input()
        if fruir in fruirs:
            print("You entered a fruit!")
        else:
            print("Sorry, I didn't know that.")

