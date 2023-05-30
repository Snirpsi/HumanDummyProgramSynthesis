#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input or enumerates user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        enumerate_user_input(sys.argv[1])
    else:
        enumerate_user_input()
        
