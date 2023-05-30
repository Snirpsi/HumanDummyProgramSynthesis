#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and multiplyes a list of numbers. """    
    
    import sys
    
    words = []
    numbers = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            break
        
        words.append(line)
        numbers.append(int(line))
    
    numbers = numbers * 2
    
    for word in words:
        print(word)
    
    print('\n'.join(words))
    
