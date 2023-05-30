#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or opens a list of words. """    
    while True:
        word = input("Enter a word: ")
        if word == "exit":
            break
        elif word == "list":
            list_words()
        elif word == "open":
            open_words()
        else:
            remove_word(word)
            
