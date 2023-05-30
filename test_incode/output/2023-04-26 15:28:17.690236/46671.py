#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or returns user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename: ")
    
    web