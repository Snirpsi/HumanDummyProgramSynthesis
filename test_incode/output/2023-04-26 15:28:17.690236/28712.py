#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words or removes words. """    
    while True:
        words = input('Enter a list of words: ')
        if words == 'exit':
            break
        else:
            words = words.split()
            words = [word for word in words if word not in STOPWORDS]
            print(' '.join(words))
            
