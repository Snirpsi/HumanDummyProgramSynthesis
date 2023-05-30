#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or returns a port. """    
    
    port = int(input("Enter a port number: "))
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving HTTP on port %d" % port)
    
    server.serve_forever()
    
