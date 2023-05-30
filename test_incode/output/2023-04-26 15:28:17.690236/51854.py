#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python get_input.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    