#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or opens user input. """    
    
    # Open user input
    words = []
    while True:
        word = input('Enter a word: ')
        if word == 'q':
            break
        else:
            words.append(word)
    
    # Print words
    for word in words:
        print(word)
    
    # Close user input
    input()
    
    # Print number of words
    print(len(words))
    
    # Close program
    exit()
    
