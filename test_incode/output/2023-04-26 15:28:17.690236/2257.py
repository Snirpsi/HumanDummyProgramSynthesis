#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), NumbersServer)
    
    print('Serving numbers from port {} ...'.format(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping')
        server.socket.close()
        sys.exit(0)
    
    print('\nStopping')
    server.socket.close()
    sys.exit(0)
    
