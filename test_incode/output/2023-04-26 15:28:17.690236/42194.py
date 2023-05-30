#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words or removes words. """    
    
    words = input("Enter a word: ")
    
    words = words.split()
    
    words = [word for word in words if word not in stopwords]
    
    print(" ".join(words))
    
