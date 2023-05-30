#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words or opens words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        words.append(line)
    
    words = list(set(words))
    
    if len(words) == 0:
        print("No words given")
        sys.exit()
    
    words.sort()
    
    word_count = 0
    
    for word in words:
        word_count += 1
        
        print("%s %s" % (word, word_count))
    
