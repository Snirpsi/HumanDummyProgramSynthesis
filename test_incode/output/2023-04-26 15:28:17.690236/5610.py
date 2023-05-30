#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words and converts user input. """    
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        else:
            word = word.lower()
            word = word.split()
            words = [word.title(), " ".join(word)]
            print(" ".join(words))
            
