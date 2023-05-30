#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers and multiplyes words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = list(map(int, numbers))
    
    words = []
    
    for number in numbers:
        words.append(str(number))
    
    print("\n".join(words))
    
