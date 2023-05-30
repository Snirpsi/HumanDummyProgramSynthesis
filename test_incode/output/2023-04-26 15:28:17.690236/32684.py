#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or converts a port. """    
    port = sys.argv[1]
    
    if port == '':
        port = '8080'
    
    httpd = HTTPServer(('', int(port)), SimpleHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    httpd.serve_forever()

<|/ file ext=.py source=github |>