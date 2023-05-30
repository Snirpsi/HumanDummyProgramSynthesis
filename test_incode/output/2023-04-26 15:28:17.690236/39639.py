#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or converts user input. """    
    while True:
        word = input('Enter a word: ')
        if word == 'exit':
            break
        else:
            word = word.lower()
            if word in words:
                words.remove(word)
            else:
                word