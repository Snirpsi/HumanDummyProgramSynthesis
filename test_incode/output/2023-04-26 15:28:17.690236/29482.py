#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words or enumerates a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        
        if word in words:
            print(word + ' is ' + words[words.index(word)])
        else:
            print(word + ' is not in list')
    
    print('Done')

<|/ file ext=.py |>