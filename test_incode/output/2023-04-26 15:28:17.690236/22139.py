#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    import sys
    
    fruits = sys.argv[1]
    
    port = int(sys.argv[2])
    
    server = HTTPServer(('', port), FruitHandler)
    
    server.serve_forever()
    
