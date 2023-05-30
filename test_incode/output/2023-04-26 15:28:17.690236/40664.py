#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and opens all ports. """    
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    server = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port 