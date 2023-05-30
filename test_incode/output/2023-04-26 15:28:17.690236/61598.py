#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or enumerates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ("", port)
    
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Serving on port {}".format(port))
    httpd.serve_forever()
    
