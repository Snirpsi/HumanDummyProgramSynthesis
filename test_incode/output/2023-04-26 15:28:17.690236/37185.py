#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and removes all ports. """    
    
    server_address = ("", 80)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
