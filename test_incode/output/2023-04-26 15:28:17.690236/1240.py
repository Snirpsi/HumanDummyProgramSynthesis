#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and enumerates a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv[0]
    
    numbers = []
    
    for line in words.splitlines():
        line = line.strip()
        
        if line == '':
            continue
        
        number, word = line.split(' ', 1)
        
        numbers.append(int(number))
    
    for number in numbers:
        print('%d %s' % (number, word))
    
