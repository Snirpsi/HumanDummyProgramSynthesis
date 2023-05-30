#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving on port %d" % port)
    httpd.serve_forever()
    
