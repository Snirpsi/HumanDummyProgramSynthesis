#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    port = int(sys.argv[1])
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    words = [w for w in words if len(w) > 1]
    
    words.sort()
    
    words = [w for w in words if len(w) > 2]
    
    words.sort()
    
    words = [w for w in words if len(w) > 3]
    
    words.sort()
    
    words = [w for w in words if len(w) > 4]
    
    words.sort()
    
    words = [w for w in words if len(w) > 5]
    
    words.sort()
    
    words = [w for w in words if len(w) > 6]
    
    words.sort()
    
    words = [w for w in words if len(w) > 7]
    
    words.sort()
    
    words = [w for w in words if len(w) > 8]
    
    words.sort()
    
    words = [w for w in words if len(w) > 9]
    
    words.sort()
    
    words = [w for w in words if len(w) > 10]
    
    words.sort()
    
    words = [w for w in words if len(w) > 11]
    
    words.sort()
    
    words = [w for w in words if len(w) > 12]
    
    words.sort()
    
    words = [w for w in words if len(w) > 13]
    
    words.sort()
    
    words = [w for w in words if len(w) > 14]
    
    words.sort()
    
    words = [w for w in words if len(w) > 15]
    
    words.sort()
    
    words = [w for w in words if len(w) > 16]
    
    words.sort()
    
    words = [w for w in words if len(w) > 17]
    
    words.sort()
    
    words = [w for w in words if len(w) > 18]
    
    words.sort()
    
    words = [w for w in words if len(w) > 19]
    
    words.sort()
    
    words = [w for w in words if len(w) > 20]
    
    words.sort()
    
    words = [w for w in words if len(w) > 21]
    
    words.sort()
    
    words = [w for w in words if len(w) > 22]