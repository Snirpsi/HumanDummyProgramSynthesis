#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python -m webserver')
        print('')
        print('Serve files from the current directory as static files')
        print('')
        print('Serve files from the specified path as static files')
        print('')
        print('