#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port %d...' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting.')
        httpd.server_close()
        
    print('\nStopped.')
    
