#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or removes user input. """    
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        else:
            word = word.lower()
            if word == "quit":
                break
            else:
                removeWord(word)
                
