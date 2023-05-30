#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers and removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving at http://127.0.0.1:%s' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down')
        server.socket.close()
    
