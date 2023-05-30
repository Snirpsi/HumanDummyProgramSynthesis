#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and returns numbers. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    numbers = []
    for line in words:
        numbers.append(int(line))
    
    print(numbers)
    
