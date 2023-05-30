#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or iterates over words. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    
    words.sort()
    
    for word in words:
        sys.stdout.write(word + '\n')
    
    sys.stdout.write('\n')
    
    
