#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('localhost', port), FruitHandler)
    
    server.serve_forever()
    
