#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), Handler)
    
    print('Serving on port %s' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print('Server stopped.')

<|/ file ext=.py filename=server.py |>