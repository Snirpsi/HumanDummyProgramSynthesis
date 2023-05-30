#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or adds numbers. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving HTTP on port {0}".format(port))
    
    server.serve_forever()
    
