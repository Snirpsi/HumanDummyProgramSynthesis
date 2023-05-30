#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    import sys
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    sys.stdout.flush()
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print('\nDone.')

<|/ file source=github ext=.py |>