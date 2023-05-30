#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words and iterates over user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    
    words.sort()
    
    for word in words:
        print(word)
    
