#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or returns user input. """    
    
    import sys
    
    port = sys.argv[1]
    
    server = HTTPServer(("", port), FruitHandler)
    server.serve_forever()
    
