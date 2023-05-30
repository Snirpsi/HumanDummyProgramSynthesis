#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and multiplyes a port. """    
    port = int(sys.argv[1])
    multiplier = int(sys.argv[2])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
