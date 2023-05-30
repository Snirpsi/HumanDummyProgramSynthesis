#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and stores numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    numbers = []
    
    for word in words:
        numbers.append(int(word))
    
    numbers = map(lambda x: x * 2, numbers)
    
    print(','.join(map(str, numbers)))
    
