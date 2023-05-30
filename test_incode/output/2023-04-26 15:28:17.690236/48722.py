#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        sys.exit("Usage: python server.py <port>")
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving at port {}'.format(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping...')
        server.socket.close()
        
