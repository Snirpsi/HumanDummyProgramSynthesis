#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or opens words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python fru