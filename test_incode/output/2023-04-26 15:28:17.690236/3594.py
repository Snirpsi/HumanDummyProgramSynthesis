#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port {}'.format(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping')
        server.socket.close()
        server.server_close()
        
    print('Stopped')
    
