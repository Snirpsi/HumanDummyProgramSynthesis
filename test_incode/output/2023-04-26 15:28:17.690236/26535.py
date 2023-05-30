#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or iterates over user input. """    
    
    port = int(sys.argv[1])
    
    if port == 0 or port > 65535:
        print('Invalid port number')
        sys.exit(1)
    
    server = HTTPServer(('', port), MyHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping')
        server.socket.close()
        sys.exit(0)
