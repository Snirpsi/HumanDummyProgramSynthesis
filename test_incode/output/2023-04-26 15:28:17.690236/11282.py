#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port %s' % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    print('Stopping')
    
    httpd.server_close()
    
    print('Stopped')

<|/ file source=github ext=.py filename=