#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits or prints a list of numbers. """    
    
    # Open the fruits file
    fruits = open('fruits.txt', 'r')
    
    # Print the list of fruits
    for line in fruits:
        print(line)
        
    # Close the fruits file
    fruits.close()
    
    # Close the program
    exit(0)
