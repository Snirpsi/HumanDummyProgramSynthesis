#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <fruit>" % sys.argv[0])
        sys.exit()
    
    fruit = sys.argv[1]
    
    fruits = load_fruits()
    
    if fruit not in fruits:
        print("Fruit %s not found." % fruit)
        sys.exit()
    
    save_