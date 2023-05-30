#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and enumerates a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s ...' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print('\nStopping HTTP on port %s ...' % port)
    
    server.socket.close()
    
    print('\nDone.')
    
