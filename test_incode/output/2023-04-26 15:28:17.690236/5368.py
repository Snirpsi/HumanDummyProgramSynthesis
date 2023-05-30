#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or calculates user input. """    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            word = word.lower()
            word = word.split()
            word = " ".join(word)
            print(word)
            
