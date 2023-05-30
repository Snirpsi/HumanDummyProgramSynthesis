#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    while True:
        words = []
        while True:
            word = input('Enter a word: ')
            if word == 'q':
                break
            words.append(word)
        print('Multiplying words:')
        for word in words:
            print(word*