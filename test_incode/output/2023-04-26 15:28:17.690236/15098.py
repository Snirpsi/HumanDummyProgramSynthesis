#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    import sys
    
    port = sys.argv[1]
    
    server = HTTPServer(("", port), FruitHandler)
    
    print("Serving at port", port)
    
    server.serve_forever()
    
