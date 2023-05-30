#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '8080'
    
    print('Serving on port %s' % port)
    
    from http.server import HTTPServer
    
    httpd = HTTPServer(('', int(port)), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
