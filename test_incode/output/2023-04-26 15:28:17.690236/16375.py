#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and prints numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split()]
    
    numbers = []
    
    for word in words:
        number = int(word)
        numbers.append(number)
        
    print("\n".join(str(number) for number in numbers))
    
