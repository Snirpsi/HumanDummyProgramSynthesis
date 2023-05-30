#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    i = 0
    while i < len(words):
        if words[i] in words:
            words.pop(i)
        else:
            i += 1
            
    print(words)
    
