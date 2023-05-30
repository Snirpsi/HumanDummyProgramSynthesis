#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        remove_user_input(sys.argv[1])
        
    else:
        
        print("No user input supplied")
        
