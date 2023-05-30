#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits or adds a list of words. """    
    
    # load words and fruits
    words = []
    fruits = []
    
    # read words and fruits from stdin
    for line in sys.stdin:
        line = line.strip()
        
        # split line into words
        words = line.split(' ')
        
        # split line into fruits
        fruits = line[:-1].split(',')
        
    # remove fruits from words
    words = filter(lambda word: word not in fruits, words)
    
    # print words
    for word in words:
        print(word)
    
    # print fruits
    for fruit in fruits:
        print(fruit)
    
    # print fruits + words
    for fruit in fruits:
        words.append(fruit)
        
    # print fruits + words + fruits
    for fruit in fruits:
        words.append(fruit)
        fruits.append(fruit)
        
    # print fruits + words + fruits + fruits
    for fruit in fruits:
        words.append(fruit)
        fruits.append(fruit)
        fruits.append(fruit)
        
    # print fruits + words + fruits + fruits + fruits
    for fruit in fruits:
        words.append(fruit)
        fruits.append(fruit)
        fruits.append(fruit)
        fruits.append(fruit)
        
    # print fruits + words + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits + fruits 