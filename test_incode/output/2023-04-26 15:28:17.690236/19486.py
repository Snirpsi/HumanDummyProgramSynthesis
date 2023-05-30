#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    import sys
    from getopt import getopt, GetoptError
    try:
        opts, args = getopt(sys.argv[1:], 'h', ['hostname=', 'port='])
    except GetoptError as err:
        print(str(err))
        sys.exit(2)
    hostname = opts[0]
    port = opts[1]
    
    numbers = []
    for arg in args:
        try:
            numbers.append(int(arg))
        except ValueError:
            print('Invalid number: %s' % arg)
            sys.exit(2)
    
    numbers.sort()
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    server.