#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds numbers and enumerates words. """    
    words = input("Enter a sentence to enumerate: ")
    words = words.split()
    
    enumerated_words = []
    for word in words:
        enumerated_words.append(word)
    
    print("The enumerated words are:")
    print(enumerated_words)
    
