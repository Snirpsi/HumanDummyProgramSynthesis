#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    for word in words:
        print('