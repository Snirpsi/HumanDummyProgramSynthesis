#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or prints user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ["hello", "world", "