#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), Handler)
    
    print('Starting server on port %s' % port)
    
    httpd.serve_forever()
    
