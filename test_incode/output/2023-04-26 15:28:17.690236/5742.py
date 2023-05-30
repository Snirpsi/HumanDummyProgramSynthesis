#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits. """    
    fruits = open_fruits()
    
    # Print the fruits we found
    for fruit in fruits:
        print(fruit)
        
    # Close the fruits we found
    for fruit in fruits:
        fruit.close()
        
    # Close the program
    