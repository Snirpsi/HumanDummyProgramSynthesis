#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        exit(1)
    
    words = []
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            words.append(line)
    
    for word in words:
        print(word)
    
