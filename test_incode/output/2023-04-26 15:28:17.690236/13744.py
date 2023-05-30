#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    
    port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
