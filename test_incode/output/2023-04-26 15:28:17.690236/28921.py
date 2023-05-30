#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and stores words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('\n'.join(words))
    print('Total words: ', len(words))
    
