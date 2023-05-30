#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words. """    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
    

<|/ file source=github |>