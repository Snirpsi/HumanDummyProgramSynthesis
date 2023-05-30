#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), Handler)
    
    print('Serving on port %s' % port)
    
    server.serve_forever()
    
