#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or converts words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(remove_word(word))
