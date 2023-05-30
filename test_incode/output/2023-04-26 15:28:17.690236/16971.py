#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python3 words.py")
        sys.exit()
    
    filename = sys.argv[1]
    
    words = []
    
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            if line:
                words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
