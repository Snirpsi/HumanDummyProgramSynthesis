#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or adds words. """    
    words = []
    while True:
        words.append(input("Enter a word: "))
        if len(words) == 3:
            break
    print("The word was", " ".join(words))
    
