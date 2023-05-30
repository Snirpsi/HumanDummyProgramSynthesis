#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words and prints words. """    
    words = input("Enter a word: ").split()
    
    multipliedWords = []
    
    for word in words:
        multipliedWords.append(word*2)
    
    print("The multiplied words are:")
    for word in multipliedWords:
        print(word)
    
