#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words or prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world', 'python', 'is', 'great']
    
    for word in words:
        print(word)
    
