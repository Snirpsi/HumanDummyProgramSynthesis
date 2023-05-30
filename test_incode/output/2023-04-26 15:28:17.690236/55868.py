#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), Handler)
    
    print('Starting web server on port %d' % port)
    
    server.serve_forever()
    
