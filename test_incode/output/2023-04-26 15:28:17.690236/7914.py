#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and returns numbers. """    
    
    port = int(sys.argv[1])
    
    print("Starting server on port {}".format(port))
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
