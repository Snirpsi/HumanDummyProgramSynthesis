#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits. """    
    
    # Read all fruits from the file
    fruits = open('fruits.txt', 'r')
    
    # Remove all fruits from the file
    fruits.close()
    
    # Print the removed fruits
    print('\nRemoved fruits:')
    
    # Iterate over the removed fruits
    for fruit in fruits:
        print('  ' + fruit)
    
    # Close the file
    fruits.close()
    
    # Close the program
    exit()
    
