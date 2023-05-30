#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits and adds numbers. """    
    while True:
        fruits = input("Enter a fruit or number: ")
        if fruits == "fruit":
            fruit = "apple"
        elif fruits == "number":
            fruit = int(input("Enter a number: "))
        else:
            print("Invalid input. Try again.")
            continue
        print("You entered", fruit)
        print("The number is", fruit