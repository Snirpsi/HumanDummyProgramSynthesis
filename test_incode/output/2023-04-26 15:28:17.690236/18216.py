#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words or converts numbers. """    
    import sys
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = range(1,10)
    
    for word in words:
        print(word)
    
