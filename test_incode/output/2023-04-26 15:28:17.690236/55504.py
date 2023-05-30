#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or converts words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            print(words[int(word) - 1])
    
