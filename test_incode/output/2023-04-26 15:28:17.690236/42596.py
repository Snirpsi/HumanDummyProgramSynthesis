#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or returns numbers. """    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
