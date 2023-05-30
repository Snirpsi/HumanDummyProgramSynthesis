#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words. """    
    words = input('Enter words: ')
    words = words.split()
    
    for word in words:
        word = word.lower()
        if word not in stopwords:
            words.append(word)
    
    print(words)
    
