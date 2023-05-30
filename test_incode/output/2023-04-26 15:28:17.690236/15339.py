#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    import sys
    from getopt import getopt, GetoptError
    opts, args = getopt(sys.argv[1:], 'h', ['host=', 'port='])
    host = 'localhost'
    port = 8000
    for opt, arg in opts:
        if opt in ('-h', '--host'):
            host = arg
        elif opt in ('-p', '--port'):
            port = int(arg)
    
    httpd = HTTPServer(
        (host, port),
        SimpleHTTPRequestHandler
    )
    print('Serving HTTP on', host, 'port', port)
    httpd.serve_forever()
    
