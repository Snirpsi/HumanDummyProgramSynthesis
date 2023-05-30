#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and enumerates a port. """    
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        
    print('Serving on port 