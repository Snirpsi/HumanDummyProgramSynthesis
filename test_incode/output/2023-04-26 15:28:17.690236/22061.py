#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and converts a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words.sort()
    
    numbers = []
    
    for word in words:
        
        number = int(word)
        
        if number > 0 and number <= 10:
            numbers.append(number)
        
    numbers.sort()
    
    for number in numbers:
        
        print('%d\t%s' % (number, words[number]))
        
