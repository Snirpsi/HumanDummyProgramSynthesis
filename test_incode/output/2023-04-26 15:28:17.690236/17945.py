#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    words = sys.argv[1:]
    
    removed = []
    for word in words:
        if word in removed:
            continue
        removed.append(word)
        
    print(' '.join(removed))

<|/ file ext=.py source=github filename=remove