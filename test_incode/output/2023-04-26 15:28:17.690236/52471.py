#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python -m webserver [port]")
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving HTTP on port %d" % port)
    httpd.serve_forever()
    
