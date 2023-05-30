#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or multiplyes a list of words. """    
    import sys
    from getopt import getopt, GetoptError
    
    try:
        opts, args = getopt(sys.argv[1:], 'hp:')
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    port = None
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('Usage: python webserver.py [-h] [-p port]')
            sys.exit()
        elif opt in ('-p', '--port'):
            port = arg
        elif opt in ('-