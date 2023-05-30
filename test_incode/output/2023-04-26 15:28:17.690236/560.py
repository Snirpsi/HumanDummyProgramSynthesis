#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or adds all ports. """    
    
    # Parse command line arguments
    port = int(sys.argv[1])
    
    # Start webserver
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start webserver
    httpd.serve_forever()
    
