#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and returns a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    print("Starting webserver on port " + str(port))
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port " + str(port))
    
    httpd.serve_forever()
    
