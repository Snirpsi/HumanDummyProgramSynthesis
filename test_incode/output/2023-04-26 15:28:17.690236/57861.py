#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words. """    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        word = word.lower()
        words.append(word)
        print("You entered 