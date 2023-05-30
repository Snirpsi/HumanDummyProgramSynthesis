#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits and enumerates user input. """    
    
    # Open the fruits.txt file
    fruits = open('fruits.txt', 'r')
    
    # Iterate over the fruits.txt file
    for line in fruits:
        # Remove all whitespace from the line
        line = line.strip()
        
        # Split line into fruit name and price
        fruit, price = line.split('\t')
        
        # Print fruit name and price
        print('{}: {}'.format(fruit, price))
        
    # Close the fruits.txt file
    fruits.close()
    
    # Close the program
    