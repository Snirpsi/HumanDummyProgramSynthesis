#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    else:
        print('Usage: ./add_word.py <word>')
        
    for word in words:
        print('%s: %d' % (word, words[word]))

<|/ file source=github ext=.py |>