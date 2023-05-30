#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words or multiplyes user input. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        if word == '':
            continue
        
        words.append(word)
        
    print('The word 