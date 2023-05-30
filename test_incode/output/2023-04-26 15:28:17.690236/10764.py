#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and converts a list of numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python webserver.py <port>')
        exit(1)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving HTTP on port {}'.format(port))
    httpd.serve_forever()
    
