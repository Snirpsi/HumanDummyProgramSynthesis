#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or multiplyes a list of numbers. """    
    port = int(sys.argv[1])
    numbers = [int(n) for n in sys.argv[2:]]
    
    if port == 0:
        port = 1
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
