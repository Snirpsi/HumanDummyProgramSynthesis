#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping')
        server.socket.close()
        
    print('\nStopped')
    
