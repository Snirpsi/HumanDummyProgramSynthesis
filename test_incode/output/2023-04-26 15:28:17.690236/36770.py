#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: fruits.py fruits.txt")
        sys.exit()
    
    with open(sys.argv[1]) as f:
        fruits = f.read().splitlines()
    
    server = HTTPServer(('', 80), FruitHandler)
    
    print('Serving on port 80...')
    server.serve_forever()
    
