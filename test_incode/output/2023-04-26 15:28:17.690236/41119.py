#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and converts a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), Handler)
    
    print("Serving HTTP on port 