#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and opens user input. """    
    
    # Open the file that contains the list of fruits.
    with open('fruits.txt', 'r') as file:
        fruits = file.read().splitlines()
    
    # Enumerate the fruits.
    for fruit in fruits:
        print('The fruit ' + fru