#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python3 remove-user-input.py <user>')
        sys.exit()
    
    user = sys.argv[1]
    
    print('Removing user input...')
    
    