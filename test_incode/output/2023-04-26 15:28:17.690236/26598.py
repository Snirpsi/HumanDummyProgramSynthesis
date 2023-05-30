#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers and removes fruits. """    
    while True:
        fruits = input("Enter a fruit or enter a number to quit: ")
        if fruits == "quit":
            break
        else:
            fruits = int(fruits)
            if fruits < 0 or fruits > 3:
                print("Invalid input")
                continue
            else:
                print("The fruit was", fruits)
                