#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or adds fruits. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit(1)
    
    words = []
    for line in open(sys.argv[1]):
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
