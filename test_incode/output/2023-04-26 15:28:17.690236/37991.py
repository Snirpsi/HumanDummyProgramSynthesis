#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and prints a list of numbers. """    
    port = 8080
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port " + str(port))
    
    httpd.serve_forever()
