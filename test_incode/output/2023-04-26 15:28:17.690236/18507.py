#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or prints a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    words = [w.strip() for w in words]
    
    server = HTTPServer(('', port), WordsServer)
    
    print('Serving on port %s' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print('Stopping server')
    
    server.socket.close()
    
    print('Done')

<|/ file source=github ext=.py |>