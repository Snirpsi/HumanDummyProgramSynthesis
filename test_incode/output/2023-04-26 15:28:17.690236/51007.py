#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        words.append(word)
        print("Added 