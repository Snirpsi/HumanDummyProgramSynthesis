#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        print('The word "' + word + '" was added to the dictionary.')
    else:
        print('No word was entered.')
    
