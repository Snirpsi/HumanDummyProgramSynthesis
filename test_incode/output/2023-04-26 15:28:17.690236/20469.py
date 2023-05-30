#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words and returns words. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            break
        
        words.append(line)
        
    words.sort()
    
    for word in words:
        print(word)
    
