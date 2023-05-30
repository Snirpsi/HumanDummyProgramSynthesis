#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words and removes words. """    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            word = word.lower()
            words = word.split()
            words.extend(words)
            words = list(set(words))
            words.sort()
            print(" ".join(words))
            
