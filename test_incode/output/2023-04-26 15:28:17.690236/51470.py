#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits or adds fruits. """    
    while True:
        fruits = input("Enter a fruit or type 'exit' to exit: ")
        if fruits == 'exit':
            break
        else:
            fruits = fruits.lower()
            if fruits == 'apple':
                print("Apple added!")
            elif fruits == 'orange':
                print("Orange added!")
            elif fruits == 'banana':
                print("Banana added!")
            else:
                print("Invalid input!")
