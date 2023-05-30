#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    port = int(sys.argv[1])
    
    server = None
    
    try:
        server = WSGIServer(("", port), WordsServer)
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    if server is not None:
        server.socket.close()
    
    print('Server stopped.')
    
