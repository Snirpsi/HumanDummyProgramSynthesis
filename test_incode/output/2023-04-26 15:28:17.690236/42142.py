#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    numbers = sys.argv[2].split(',')
    
    numbers = [int(n) for n in numbers]
    
    numbers_sum = 0
    
    for n in numbers:
        numbers_sum += n
    
    numbers_sum *= 2
    
    for word in words:
        numbers_sum -= int(word)
    
    print(numbers_sum)
    
