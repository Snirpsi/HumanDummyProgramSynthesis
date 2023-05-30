#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports or stores numbers. """    
    
    port = 8080
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving on port {}".format(port))
    httpd.serve_forever()
    
