#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    words = sys.argv[1:]
    
    words = words.split(',')
    
    removed = []
    for word in words:
        if word not in removed:
            removed.append(word)
    
    print(','.join(removed))

<|/ file ext=.py |>