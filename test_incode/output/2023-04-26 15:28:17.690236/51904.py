#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), Handler)
    
    print('Serving HTTP on port %s' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print('Server stopped')
    
