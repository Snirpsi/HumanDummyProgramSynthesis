#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or adds a port. """    
    while True:
        words = input('Enter a word: ')
        if words:
            words = words.split()
            words = [word for word in words if word]
            print(' '.join(words))
        else:
            break
