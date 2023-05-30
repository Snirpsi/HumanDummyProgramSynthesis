#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit()
    
    words = []
    
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            words.append(arg)
        else:
            words.append(arg.strip())
    
    if len(words) == 0:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit()
    
    words = list(set(words))
    
    words.sort()
    
    if len(words) > 10:
        print("Too many words: %s" % ' '.join(words))
        sys.exit()
    
    word