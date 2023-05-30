#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 removeUserInput.py <username>')
        exit(1)
    
    username = sys.argv[1]
    
    print('Removing user input for user "{}".'.format(username))
    
    removeUserInput(username)
    
    print('Done.')
    
