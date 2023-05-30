#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and returns a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <wordlist>" % sys.argv[0])
        sys.exit()
    
    wordlist = sys.argv[1]
    
    words = []
    for line in open(wordlist, 'r'):
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    word