#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and multiplyes a port. """    
    port = int(sys.argv[1])
    
    # Create a server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start it
    httpd.serve_forever()
