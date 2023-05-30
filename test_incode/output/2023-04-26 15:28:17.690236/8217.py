#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or prints a port. """    
    
    port = int(sys.argv[1])
    
    if port == 0:
        port = 80
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port %d" % port)
    httpd.serve_forever()
    
