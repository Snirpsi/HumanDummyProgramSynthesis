#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    i = 0
    while i < len(words):
        words[i] = words[i] * 10
        i += 1
        
    print(''.join(words))
    
