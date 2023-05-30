#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('You entered', len(words), 'words.')
    print('Here are your words: ')
    for word in words:
        print(word)
    print('