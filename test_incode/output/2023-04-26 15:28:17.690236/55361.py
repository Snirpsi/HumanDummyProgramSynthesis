#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = []
    
    print('Serving on port %s' % port)
    
    server = HTTPServer(('', port), NumbersHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print('\n