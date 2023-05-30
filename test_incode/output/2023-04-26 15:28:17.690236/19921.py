#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and calculates fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = list(set(words))
    
    fruits = []
    
    for word in words:
        fruits.append(word)
    
    fruits.sort()
    
    words = [word for word in words if word not in fruits]
    
    print("\n".join(words))
    
