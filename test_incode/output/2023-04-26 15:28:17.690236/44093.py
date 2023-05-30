#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or opens words. """    
    while True:
        word = input("Enter a word: ")
        if word == 'exit':
            break
        else:
            print(word)
            
