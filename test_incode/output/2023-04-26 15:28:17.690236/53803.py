#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and stores user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'quit':
            break
        
    print('\nThe list of words is:')
    for word in words:
        print(word)
    
    print('\nThe user input was:')
    print(word