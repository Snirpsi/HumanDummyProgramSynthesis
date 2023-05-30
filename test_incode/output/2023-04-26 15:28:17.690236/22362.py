#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and calculates numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python -m SimpleHTTPServer <port>")
        sys.exit(1)
    
    httpd = HTTPServer(('', int(sys.argv[1])), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port " + str(httpd.server_