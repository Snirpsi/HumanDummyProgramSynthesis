#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    fruits = list('apple')
    
    server = HTTPServer(('', port), FruitHandler)
    
    print('Serving on port 