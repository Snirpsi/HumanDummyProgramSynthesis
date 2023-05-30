#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and calculates user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
        
    print('\n'.join([word for word in words if len(word) > 2]))
    
    