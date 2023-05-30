#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words or multiplyes words. """    
    
    # Read user input from stdin
    words = input().split()
    
    # Multiply words by 2
    words = [x*2 for x in words]
    
    # Print the result
    print(' '.join(words))
    
