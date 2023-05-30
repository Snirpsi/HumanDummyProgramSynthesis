#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input and converts a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), MyHandler)
    
    print("Serving at port", port)
    
    server.serve_forever()
    
