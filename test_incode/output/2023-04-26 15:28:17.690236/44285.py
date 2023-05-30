#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <fruit>' % sys.argv[0])
        exit(1)
    
    fruit = sys.argv[1]
    
    fruits = fruit.split()
    
    fruits.sort()
    
    words = []
    
    for fruit in fruits:
        word = '%s %s' % (fruit, 