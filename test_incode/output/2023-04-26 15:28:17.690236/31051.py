#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or enumerates words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1:]
    
    numbers = map(int, words)
    
    words = list(set(words))
    
    words.sort()
    
    for number in numbers:
        sys.stdout.write(str(number))
        sys.stdout.write(' ')
        sys.stdout.write(''.join(words))
        sys.stdout.write('\n')
    
