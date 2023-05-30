#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), NumbersHandler)
    
    server.serve_forever()
    
