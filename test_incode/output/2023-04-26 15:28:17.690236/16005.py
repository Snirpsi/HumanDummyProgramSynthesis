#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or converts a port. """    
    port = int(sys.argv[1])
    
    # Start a web server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Wait forever
    httpd.serve_forever()
