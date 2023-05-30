#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and iterates over user input. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    print('Your words are:')
    for word in words:
        print(word)
    print('')
    print('Press q to quit.')
    
