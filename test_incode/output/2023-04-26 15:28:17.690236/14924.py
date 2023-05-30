#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores fruits or prints a list of words. """    
    
    # Read input from stdin
    fruit = sys.stdin.readline().strip()
    
    # Print the list of fruits
    print(' '.join(fruits))
    
    # Print the fruit itself
    print(fruit)
    
    # Print the fruit and its count
    print(' '.join(fruits), count)
    
    # Print the fruit and its count and 