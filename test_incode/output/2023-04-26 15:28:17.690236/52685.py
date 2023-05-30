#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or prints a list of numbers. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %d ...' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print('\nStopping HTTP on port %d ...' % port)
    
    