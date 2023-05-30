#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or converts fruits. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <fruit>' % sys.argv[0])
        sys.exit()
    
    fruit = str(sys.argv[1])
    
    if fruit == '':
        print('Usage: %s <fruit>' % sys.argv[0])
        sys.exit()
    
    fruits = list(fruit)
    
    print('Content-Type: text/plain')
    print('')
    
    for fruit in fruits:
        print('%s: %d' % (fruit, 