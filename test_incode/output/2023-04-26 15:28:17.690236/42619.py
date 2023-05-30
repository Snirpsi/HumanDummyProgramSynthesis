#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words and enumerates words. """    
    words = []
    
    # Add words to the list
    words.append(input("Enter a word: "))
    words.append(input("Enter another word: "))
    words.append(input("Enter yet another word: "))
    
    # Enumerate words in the list
    for word in words:
        print(word)
    
    # Print the final list
    print(words)
    
    # 