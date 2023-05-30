#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Starting web server on port %d...' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping web server')
        httpd.server_close()
    
    print('\nStopped web server')
    
