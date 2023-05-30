#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or removes user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <fruit|user>" % sys.argv[0])
        sys.exit()
    
    fruit = sys.argv[1]
    
    if fruit == 'user':
        remove_user_input()
    else:
        remove_fruit(fruit)
    
