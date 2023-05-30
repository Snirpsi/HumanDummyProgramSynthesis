#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and iterates over a list of numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    i = 0
    while True:
        i += 1
        print('Word:', words[i])
        
        if i == len(words):
            break
        
        word