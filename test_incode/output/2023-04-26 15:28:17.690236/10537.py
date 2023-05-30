#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input and enumerates words. """    
    
    # read user input
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        words.append(word)
    
    # enumerate words
    for word in words:
        print(word)
        
    # 