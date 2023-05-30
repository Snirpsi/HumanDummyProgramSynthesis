#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or stores words. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        words.append(word)
        print('The word "' + word + '" was stored.')
    
    print('The words are:')
    for word in words:
        print(word)
    
    print('\nThe word "quit" was 