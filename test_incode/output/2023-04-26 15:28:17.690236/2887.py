#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping')
        httpd.server_close()
        
    print('Stopped')
    
