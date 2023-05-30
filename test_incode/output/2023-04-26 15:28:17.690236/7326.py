#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python -m SimpleWebServer")
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    print("Serving on port {}".format(port))
    
    httpd = HTTPServer(("", port), SimpleWebServer)
    httpd.serve_forever()
