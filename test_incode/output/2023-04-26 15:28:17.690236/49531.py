#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and stores a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1].split()
    
    numbers = []
    
    for word in words:
        numbers.append(int(word) * 2)
    
    print(numbers)
    
