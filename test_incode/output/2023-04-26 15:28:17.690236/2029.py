#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits or opens numbers. """    
    while True:
        print("Fruits")
        fruits = input("Enter a fruit or number: ")
        if fruits == "fruit":
            fruits = input("Enter a fruit or number: ")
            fruits = fruits.upper()
            print(