#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or removes a list of words. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    
    words = list(set(words))
    
    if len(sys.argv) == 2:
        words = words[:]
        words.append(sys.argv[1])
    
    words = list(set(words))
    
    if len(words) == 0:
        print("No words given")
        sys.exit()
    
    words.sort()
    
    word