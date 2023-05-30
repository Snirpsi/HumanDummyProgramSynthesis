#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and converts words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1].split()
    
    numbers = [int(word) for word in words]
    
    words = [str(number) for number in numbers]
    
    print("\n".join(words))
    
