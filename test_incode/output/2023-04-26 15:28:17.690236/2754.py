#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or opens words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    words.sort()
    
    sys.stdout.write("\n".join(words))
    
    
