#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or opens numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Please enter the name of the file to open: ")
    
    webbrowser.open_new( filename )
    
