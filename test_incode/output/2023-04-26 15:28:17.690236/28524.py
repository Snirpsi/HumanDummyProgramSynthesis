#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and adds numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), Handler)
    server.serve_forever()
    
