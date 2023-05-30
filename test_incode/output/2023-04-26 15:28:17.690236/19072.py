#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input or stores words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        words.append(word)
    
    multiplier = 1
    
    for word in words:
        multiplier = multiplier * int(word)
    
    print('The product is', multiplier)
    
