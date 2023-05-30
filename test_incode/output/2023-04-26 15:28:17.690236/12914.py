#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and stores fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    fruits = []
    
    for i in range(1, port+1):
        fruits.append(i)
    
    print('Serving on port {}'.format(port))
    
    for fruit in fruits:
        print('Fruit {}