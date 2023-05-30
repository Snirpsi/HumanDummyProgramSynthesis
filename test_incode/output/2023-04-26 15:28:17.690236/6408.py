#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and adds numbers. """    
    words = []
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words = line.split(' ')
        
        for word in words:
            numbers.append(int(word))
            
    numbers.sort()
    
    for number in numbers:
        word = '{}'.format(number)
        words.append(word)
        
    print(' '.join(words))
    
