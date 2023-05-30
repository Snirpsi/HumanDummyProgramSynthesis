#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or converts a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [words...]' % sys.argv[0])
        exit(1)
    
    words = [w.strip() for w in sys.argv[1:]]
    
    fruit = Fruit()
    
    for word in words:
        fruit.add(word)
    
    fruit.convert()
    
    print('\nDone.')
    
