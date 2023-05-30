#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port %s' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down...')
        httpd.server_close()
    
    print('\nStopping...')
    
    httpd.server_close()
    
    print('\nDone.')
    
