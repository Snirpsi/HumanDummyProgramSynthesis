#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words or enumerates user input. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            words.append(word)
    print('The words are: ')
    for word in words:
        print(word)
    print('')
    
<|/ file filename=