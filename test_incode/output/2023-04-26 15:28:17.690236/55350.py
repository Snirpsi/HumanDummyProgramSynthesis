#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits or prints fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        fruits = sys.argv[1:]
        
        print('\n'.join(sorted([