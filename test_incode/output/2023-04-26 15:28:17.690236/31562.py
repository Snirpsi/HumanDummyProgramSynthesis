#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    server = BaseHTTPServer.HTTPServer(('localhost', port), MyHandler)
    print('Serving on port %s' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down')
        server.socket.close()
    
    print('\nStopping')
    
    server.socket.close()
    
