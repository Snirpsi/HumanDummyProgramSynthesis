#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports or prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['hello', 'world']
    
    for word in words:
        print('The word "%s" is' % word)
        print('%d times 