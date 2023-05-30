#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    from getopt import getopt, GetoptError
    try:
        opts, args = getopt(sys.argv[1:], '', ['port=', 'host=', 'help'])
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    port = int(opts.get('port', 8080))
    host = '127.0.0.1'
    for o, a in opts:
        if o == '--port':
            port = int(