#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words or prints user input. """    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        else:
            print(word*2)
    
