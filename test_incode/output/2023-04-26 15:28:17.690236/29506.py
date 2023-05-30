#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            continue
        words.append(line)
    
    words = " ".join(words)
    
    words = words.split()
    
    words = [w for w in words if w not in sys.argv[1:]]
    
    print("\n".join(words))

<|/ file source=github ext=.py |>