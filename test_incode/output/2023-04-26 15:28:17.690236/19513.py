#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or prints a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = input("Enter a word: ")
    
    if word == 'exit':
        sys.exit(0)
    
    words = [word.lower()]
    
    for letter in word:
        if letter.isalpha():
            words.append(letter)
    
    print(" ".join(words))
    
