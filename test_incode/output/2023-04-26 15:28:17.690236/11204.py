#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and adds user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    
    words.sort()
    
    print('\n'.join(words))
    
