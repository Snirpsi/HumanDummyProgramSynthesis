#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <fruits>' % sys.argv[0])
        sys.exit(1)
    
    fruits = sys.argv[1:]
    
    server = FruitServer(fruits)
    server.serve_forever()
    
