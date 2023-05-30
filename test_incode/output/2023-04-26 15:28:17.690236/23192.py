#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    from getopt import getopt, GetoptError
    
    try:
        opts, args = getopt(sys.argv[1:], 'h', ['help'])
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    
    for o, a in opts:
        if o == '-h':
            print('Usage: python webserver.py [-h] [-p PORT]')
            sys.exit()
        elif o == '-p':
            port = a
        else:
            print('Unrecognized option: ' + o)
            sys.exit()
    
    