#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words. """    
    words = ['hello', 'world', 'how', 'are', 'you', 'today', '?']
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            print(words[words.index(word)])
            
