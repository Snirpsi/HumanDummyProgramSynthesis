#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words and removes words. """    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        word = word.lower()
        word = word.split()
        word = [word for word in word if word not in stopwords]
        print(' '.join(word))
