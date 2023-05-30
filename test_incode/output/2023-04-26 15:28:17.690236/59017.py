#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or converts words. """    
    words = []
    
    for word in sys.argv[1:]:
        if word == '-':
            words.append(sys.stdin.readline().strip())
        else:
            words.append(word)
    
    words = ' '.join(words)
    
    words = words.split()
    
    words = filter(None, words)
    
    words = list(set(words))
    
    words.sort()
    
    print(words)

<|/ file ext=.py |>