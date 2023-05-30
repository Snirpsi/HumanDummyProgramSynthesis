#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and enumerates words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <wordlist>' % sys.argv[0])
        sys.exit()
    
    wordlist = sys.argv[1]
    
    words = []
    for line in open(wordlist):
        line = line.strip()
        if not line or line[0] == '#':
            continue
        words.append(line)
    
    words.sort()
    
    enumerated_words = []
    
    for word in words:
        enumerated_words.append(word)
        
    print('\n'.join(enumerated_words))
    
