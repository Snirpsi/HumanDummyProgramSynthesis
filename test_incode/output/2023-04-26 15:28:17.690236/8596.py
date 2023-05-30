#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or converts a port. """    
    while True:
        word = input("Enter a word: ")
        if word == 'exit':
            break
        else:
            word = word.lower()
            if word == 'help':
                help()
            else:
                convert(word)

<|/ file filename=word