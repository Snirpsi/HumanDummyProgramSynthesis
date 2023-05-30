#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or opens a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    
    for word in words:
        print(word)
    
    if port > 0:
        with open('words.txt', 'w') as words:
            for word in words:
                word