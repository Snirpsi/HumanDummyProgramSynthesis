#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    server = HTTPServer(('', 80), WordsHandler)
    
    print('Serving on port 80')
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting...')
        server.socket.close()
        server.server_close()
        sys.exit(0)
    
    print('\nWords: %s' % words)
    
    
