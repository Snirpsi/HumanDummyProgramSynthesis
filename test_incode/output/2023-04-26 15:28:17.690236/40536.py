#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and iterates over a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        number, word = line.split('\t')
        
        numbers.append(int(number))
        words.append(word)
    
    numbers.sort()
    words.sort()
    
    for number in numbers:
        for word in words:
            print('%s\t%s' % (number, word))
        
        print('')
        
