#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits or multiplyes user input. """    
    while True:
        fruit = input("Enter a fruit name: ")
        if fruit == '':
            break
        else:
            print("You entered " + fruit)
            