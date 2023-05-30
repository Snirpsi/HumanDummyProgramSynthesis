#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    port = 8080
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving on port %d" % port)
    httpd.serve_forever()
    
