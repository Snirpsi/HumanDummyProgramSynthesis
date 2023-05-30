#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 input.py <message>")
        sys.exit()
    
    message = sys.argv[1]
    
    print("You said: " + message)
    
