#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port ' + str(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping server')
        server.socket.close()
        sys.exit(0)
    
    print('\nStopping server')
    server.socket.close()
    sys.exit(0)
