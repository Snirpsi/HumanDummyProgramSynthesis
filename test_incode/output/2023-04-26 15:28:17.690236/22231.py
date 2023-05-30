#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    words = [w for w in words if len(w) > 0]
    
    numbers = map(int, words) # Convert words to numbers
    
    numbers = map(lambda x: x*2, numbers) # Multiply each number by 2
    
    numbers = list(map(str, numbers)) # Convert numbers to strings
    
    print("\n".join(numbers))
    
