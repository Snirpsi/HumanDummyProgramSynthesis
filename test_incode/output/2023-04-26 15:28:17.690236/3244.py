#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or stores a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <wordfile>' % sys.argv[0])
        sys.exit()
    
    wordfile = sys.argv[1]
    
    words = []
    
    with open(wordfile) as wordfile:
        for line in wordfile:
            line = line.strip()
            
            if line == '':
                continue
            
            if line[0].isupper():
                words.append(line