#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or opens user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Please enter the file name: ")
    
    web