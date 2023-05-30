#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <fruits.txt>" % sys.argv[0])
        sys.exit()
    
    fruits = sys.argv[1].splitlines()
    
    words = []
    
    for fruit in fruits:
        fruits.remove(fruit)
        
        words += [' '.join(fruits)]
    
    print('\n'.join(words))
    
