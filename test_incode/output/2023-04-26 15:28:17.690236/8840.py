#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    words = []
    
    words.append(input("Enter a word: "))
    
    words = words + list(filter(lambda x: len(x) > 0, words))
    
    words = words + list(filter(lambda x: len(x) < 3, words))
    
    words = words + list(filter(lambda x: len(x) > 3, words))
    
    words = words + list(filter(lambda x: len(x) == 3, words))
    
    words = words + list(filter(lambda x: len(x) == 4, words))
    
    words = words + list(filter(lambda x: len(x) == 5, words))
    
    words = words + list(filter(lambda x: len(x) == 6, words))
    
    words = words + list(filter(lambda x: len(x) == 7, words))
    
    words = words + list(filter(lambda x: len(x) == 8, words))
    
    words = words + list(filter(lambda x: len(x) == 9, words))
    
    words = words + list(filter(lambda x: len(x) == 10, words))
    
    words = words + list(filter(lambda x: len(x) == 11, words))
    
    words = words + list(filter(lambda x: len(x) == 12, words))
    
    words = words + list(filter(lambda x: len(x) == 13, words))
    
    words = words + list(filter(lambda x: len(x) == 14, words))
    
    words = words + list(filter(lambda x: len(x) == 15, words))
    
    words = words + list(filter(lambda x: len(x) == 16, words))
    
    words = words + list(filter(lambda x: len(x) == 17, words))
    
    words = words + list(filter(lambda x: len(x) == 18, words))
    
    words = words + list(filter(lambda x: len(x) == 19, words))
    
    words = words + list(filter(lambda x: len(x) == 20, words))
    
    words = words + list(filter(lambda x: len(x) == 21, words))
    
    words = words + list(filter(lambda x: len(x) == 22, words))
    
    words = words + list(filter(lambda x: len(x) == 23, words))
    
    words = words + list(filter(lambda x: len(x) == 24, words))
    
    words = words + list(filter(lambda x: len(x) == 25, words))
    
    words = words + list(filter(lambda x: len(x) == 26, words))
    
    words = words + list(filter(lambda x: len(x) == 27, words))
    
    words = words + list(filter(lambda x: len(x) == 28, words))
    
    words = words + list(filter(lambda x: len(x) == 29, words))
    
    words = words + list(filter(lambda x: len(x) == 30, words))