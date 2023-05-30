#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    
    # Get the command line arguments
    args = sys.argv[1:]
    
    # Parse the arguments
    words = []
    for arg in args:
        words.append(arg)
    
    # Multiply each word in the list
    product = 1
    for word in words:
        product *= word
    
    # Print the result
    print(product)
    
