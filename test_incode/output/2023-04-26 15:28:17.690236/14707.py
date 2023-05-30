#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or stores a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    numbers = []
    for number in words:
        numbers.append(int(number))
    
    print(numbers)
    
