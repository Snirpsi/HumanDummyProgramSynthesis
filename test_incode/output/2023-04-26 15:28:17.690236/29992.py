#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and adds a list of numbers. """    
    
    import sys
    
    wordlist = sys.argv[1]
    
    numbers = []
    
    for line in wordlist.splitlines():
        line = line.strip()
        
        if line == '':
            continue
        
        numbers.append(int(line))
    
    numbers = numbers + [0] * (len(wordlist) - len(numbers))
    
    print('\n'.join(map(str, numbers)))
    
