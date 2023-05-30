#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or removes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python -m webserver.py <port>')
        sys.exit()
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving HTTP on port {0.