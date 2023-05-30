#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or stores a port. """    
    port = int(sys.argv[1])
    
    # Start a server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Run the server
    httpd.serve_forever()
    
