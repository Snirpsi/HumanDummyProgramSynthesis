#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or opens user input. """    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            print(remove_word(word))
            
