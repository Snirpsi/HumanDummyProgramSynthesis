#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port. """    
    port = sys.argv[1]
    
    httpd = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Serving HTTP on port ", port)
    httpd.serve_forever()
