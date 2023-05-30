#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words and calculates a port. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <filename>' % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    words = []
    with open(filename) as f:
        for line in f:
            words = words + line.split()
    
    words = list(set(words))
    
    words.sort()
    
    port = 0
    
    for word in words:
        if word == '':
            port += 1
        else:
            port += word.count('