#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port ' + str(port) + '...')
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting.')
        
    server.server_close()
    
    print('\nDone.')
    
