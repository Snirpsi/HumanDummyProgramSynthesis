#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or iterates over a list of words. """    
    import sys
    port = sys.argv[1]
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    words.sort()
    for word in words:
        print(word, end=' ')
        if port == '':
            break
        