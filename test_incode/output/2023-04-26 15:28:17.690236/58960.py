#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    while True:
        words = input('Enter a word: ')
        if words:
            words = words.split()
            words = [word for word in words if word not in stopwords]
            print(' '.join(words))
        else:
            break
