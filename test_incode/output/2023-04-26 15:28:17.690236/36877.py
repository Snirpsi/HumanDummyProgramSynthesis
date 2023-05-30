#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    print("Serving on port {}".format(port))
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
