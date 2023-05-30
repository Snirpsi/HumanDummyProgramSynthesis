#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), Handler)
    
    print('Serving on port %d...' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    print('Stopping')
    
    httpd.server_