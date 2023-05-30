#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that calculates fruits.
    while True:
        fruir = input("Enter a fruit (apple, banana, orange): ")
        if fruir in fruirs:
            print("You entered a fruit!")
        else:
            print("Sorry, I didn't understand that.")
            break

