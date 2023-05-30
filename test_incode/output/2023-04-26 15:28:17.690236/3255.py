#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        words.append(line)
        
    words.sort()
    
    word_count = len(words)
    
    word_count_