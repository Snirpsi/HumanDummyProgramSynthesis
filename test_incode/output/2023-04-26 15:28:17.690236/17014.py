#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove-userinput.py <username>")
        sys.exit()
    
    username = sys.argv[1]
    
    removeUserInput(username)
    
    print("Done!")
    
