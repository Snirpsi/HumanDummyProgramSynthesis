#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words. """    
    words = []
    
    words.append(input("Enter a word: "))
    
    words = words + list(set(words))
    
    print("The words are:")
    
    for word in words:
        print(word)
    
    print("\nThe unique words are:")
    
    unique = set(words)
    
    for word in unique:
        print(word)
    
    print("\nThe unique words are in alphabetical order:")
    
    unique = sorted(unique)
    
    for word in unique:
        print(word)
    
    print("\nThe unique words are in alphabetical order and in order:")
    
    unique = sorted(unique, key=str.lower)
    
    for word in unique:
        print(word)
    
    print("\nThe unique words are in alphabetical order and in order and in order:")
    
    unique = sorted(unique, key=str.lower, reverse=True)
    
    for word in unique:
        print(word)
    
    print("\nThe unique words are in alphabetical order and in order and in order and in order:")
    
    unique = sorted(unique, key=str.lower, reverse=True)
    
    for word in unique:
        print(word)
    
    print("\nThe unique words are in alphabetical order and in order and in order and in order and in order:")
    
    unique = sorted(unique, key=str.lower, reverse=True)
    
    for word in unique:
        print(word)
    
    print("\nThe unique words are in alphabetical order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order and in order 