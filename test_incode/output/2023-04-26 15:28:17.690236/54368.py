#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s...' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    print('Stopping HTTP on port %s...' % port)
    
    httpd.server_close()
    
    print('Stopped.')
    
