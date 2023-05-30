#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words and iterates over a port. """    
    import sys
    port = int(sys.argv[1])
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    words = list(set(words))
    words.sort()
    
    for word in words:
        sys.stdout.write('{}\n'.format(word))
        sys.stdout.flush()
        
    
<|/ file source=github filename=wordcount.py |>