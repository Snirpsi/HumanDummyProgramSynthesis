#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words or prints user input. """    
    words = []
    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        words.append(word)
    
    print("\n".join(words))
    
