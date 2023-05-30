#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1].split()
    
    numbers = []
    
    for word in words:
        numbers.append(int(word) * len(words))
    
    print('\n'.join(map(str, numbers)))
    
