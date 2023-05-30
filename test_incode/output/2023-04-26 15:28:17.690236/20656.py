#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <wordlist>' % sys.argv[0])
        sys.exit()
    
    wordlist = sys.argv[1]
    
    words = [w.lower() for w in open(wordlist)]
    
    words = [w for w in words if len(w) > 1]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 2]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 3]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 4]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 5]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 6]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 7]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 8]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 9]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 10]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 11]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 12]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 13]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 14]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 15]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 16]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 17]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 18]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 19]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 20]
    
    words = sorted(words)
    
    words = [w for w in words if len(w) > 2