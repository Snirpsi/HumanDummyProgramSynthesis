#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    port = int(sys.argv[1])
    print("Starting server on port %d" % port)
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
