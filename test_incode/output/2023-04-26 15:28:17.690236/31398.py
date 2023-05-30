#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input and returns a port. """    
    port = int(input("Enter a port number: "))
    
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    print("Serving at port {}".format(port))
    
    server.serve_forever()
