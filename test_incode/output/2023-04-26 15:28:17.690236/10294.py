#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', int(port)), SimpleHTTPRequestHandler)
    
    print("Serving on port %d" % port)
    httpd.serve_forever()
    
