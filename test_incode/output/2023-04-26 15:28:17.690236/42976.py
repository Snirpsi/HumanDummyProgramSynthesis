#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words and adds words. """    
    import sys
    words = []
    for word in sys.argv[1:]:
        words.append(word.lower())
    
    words = list(set(words))
    
    words = list(filter(lambda word: len(word) > 2, words))
    
    words = list(filter(lambda word: len(word) <= 2, words))
    
    words = list(filter(lambda word: word not in STOPWORDS, words))
    
    words = list(filter(lambda word: len(word) > 1, words))
    
    words = list(filter(lambda word: len(word) <= 1, words))
    
    words = list(filter(lambda word: word not in STOPWORDS, words))
    
    words = list(filter(lambda word: len(word) > 2, words))
    
    words = list(filter(lambda word: len(word) <= 2, words))
    
    words = list(filter(lambda word: word not in STOPWORDS, words))
    
    words = list(filter(lambda word: len(word) > 1, words))
    
    words = list(filter(lambda word: len(word) <= 1, words))
    
    words = list(filter(lambda word: word not in STOPWORDS, words))
    
    words = list(filter(lambda word: len(word) > 2, words))
    
    words = list(filter(lambda word: len(word) <= 2, words))
    
    words = list(filter(lambda word: word not in STOPWORDS, words))
    
    words = list(filter(lambda word: len(word) > 1, words))
    
    words = list(filter(lambda word: len(word) <= 1, words))
    
    words = list(filter(lambda word: word not in STOPWORDS, words))
    
    words = list(filter(lambda word: len(word) > 2, words))
    
    words = list(filter(lambda word: len(word) <= 2, words))
    
    words = list(filter(lambda word: word not in STOPWORDS, words))
    
    words = list(filter(lambda word: len(word) > 1, words))
    
    words = list(filter(lambda word: len(word) <= 1, words))
    
    words = list(filter(lambda word: word not in STOPWORDS, words))
    
    words = list(filter(lambda word: len(word) > 2, words))
    
    words = list(filter(lambda word: len(word) <= 2, words))
    
    words = list(filter(lambda word: word not in STOPWORDS, words))
    
    words = list(filter(lambda word: len(word) > 1, words))
    
    words = list(filter(lambda word: len(word) <= 1, words))
    
    words = list(filter(lambda word: word not in STOPWORDS, words))
    
    words = list(filter(lambda word: len(word) > 2, words))
    
    words = list(filter(lambda word: 