#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('The words are:')
    for word in words:
        print(word)
    print('')
    print('Press any key to exit')
    input()
