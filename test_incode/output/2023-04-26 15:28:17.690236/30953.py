#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or adds numbers. """    
    while True:
        word = input("Enter a word: ")
        if word == 'exit':
            break
        else:
            print(word)
            