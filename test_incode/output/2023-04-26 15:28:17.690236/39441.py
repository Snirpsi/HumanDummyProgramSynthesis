#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or converts fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <fruit>" % sys.argv[0])
        sys.exit()
    
    fruit = sys.argv[1]
    
    if fruit == 'convert':
        fruits = convert_fruits()
    elif fruit == 'store':
        fruits = store_fruits()
    else:
        print("Usage: %s <fruit>" % sys.argv[0])
        sys.exit()
    
    for fruit in fruits:
        print("%s -> %s" % (fruit, fruits[fruit]))
    
