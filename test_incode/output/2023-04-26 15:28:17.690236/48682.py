#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or converts user input. """    
    while True:
        fruits = input("Enter fruit or type 'quit' to quit: ")
        if fruits == 'quit':
            break
        else:
            print(calculate_fruits(fruits))

<|/ file filename=