#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    port = int(sys.argv[1])
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    words.sort()
    words = [w for w in words if w]
    words = [w for w in words if len(w) > 2]
    words = [w for w in words if len(w) == 2]
    words = [w for w in words if len(w) > 1]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    words = [w for w in words if len(w) == 0]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    words = [w for w in words if len(w) == 0]
    words = [w for w in words if len(w) > 1]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    words = [w for w in words if len(w) == 0]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    words = [w for w in words if len(w) == 0]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    words = [w for w in words if len(w) == 0]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    words = [w for w in words if len(w) == 0]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    words = [w for w in words if len(w) == 0]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    words = [w for w in words if len(w) == 0]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    words = [w for w in words if len(w) == 0]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    words = [w for w in words if len(w) == 0]
    words = [w for w in words if len(w) == 1]
    words = [w for w in words if len(w) > 0]
    