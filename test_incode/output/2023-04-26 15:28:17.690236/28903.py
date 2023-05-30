#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and calculates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = 'localhost'
    
    port = 8080
    
    httpd = HTTPServer(
        (host, port),
        SimpleHTTPRequestHandler
    )
    
    print('Serving on port 8080')
    
    httpd.serve_forever()
    
