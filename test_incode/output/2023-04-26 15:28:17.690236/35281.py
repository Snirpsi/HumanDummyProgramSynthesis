#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and adds a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    print("Starting webserver on port {}".format(port))
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port {}".format(port))
    
    httpd.serve_forever()
    
