#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers and iterates over words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<word>]" % sys.argv[0])
        sys.exit(0)
    
    file = sys.argv[1]
    word = sys.argv[2] if len(sys.argv) > 2 else None
    
    file = open(file, 'r')
    
    for line in file:
        line = line.strip()
        
        if word and line == word:
            print(line)
            continue
        
        words = line.split()
        
        for word in words:
            print(word)
    
    file.close()
    
