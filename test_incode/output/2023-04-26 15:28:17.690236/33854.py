#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores user input and removes a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'quit':
            break
        
    print('The words are:')
    
    for word in words:
        print(word)
    
    print('')
    
    removed = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word not in words:
            removed.append(word)
    
    print('The words are:')
    
    for word in removed:
        print(word)
    
    print('')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    