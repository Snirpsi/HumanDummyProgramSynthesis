#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = sys.argv[1].split()
    
    words = [word.strip() for word in words]
    
    words = [word for word in words if word not in numbers]
    
    print("\n".join(words))
    
    
