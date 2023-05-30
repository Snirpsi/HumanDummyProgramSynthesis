#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words or converts numbers. """    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
