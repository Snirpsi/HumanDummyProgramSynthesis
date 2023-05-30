#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port %s' % port)
    
    httpd.serve_forever()

<|/ file filename=server.py |>