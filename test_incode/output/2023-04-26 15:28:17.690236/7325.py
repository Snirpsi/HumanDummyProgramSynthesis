#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or multiplyes a port. """    
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            words.append(word)
    print('\n'.join([str(x) for x in words]))
    
