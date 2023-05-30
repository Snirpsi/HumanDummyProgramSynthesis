#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = find_ports()
    
    # Create a simple webserver
    httpd = HTTPServer(('', ports[0]), SimpleHTTPRequestHandler)
    
    # Listen for requests
    httpd.serve_forever()
    
