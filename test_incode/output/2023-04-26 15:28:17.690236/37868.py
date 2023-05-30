#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and converts a port. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    port = int(sys.argv[1])
    
    words = sorted(words, key = lambda word: word.lower())
    
    for word in words:
        print(word, end=' ')
        
        if port == int(word):
            print(word, end=' ')
    
