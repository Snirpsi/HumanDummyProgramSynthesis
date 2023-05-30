#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from getopt import getopt, GetoptError
    
    try:
        opts, args = getopt(sys.argv[1:], 'h', ['help'])
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    words = []
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('Usage: python 