#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits. """    
    
    # Open the fruit file
    fruit = open_fruit("fruits.txt")
    
    # Print the fruit name
    print(fruit.readline())
    
    # Close the fruit file
    fruit.close()
    
