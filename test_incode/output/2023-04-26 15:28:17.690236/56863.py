#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words and stores user input. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    word = ''
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word in words:
            print(word)
        else:
            print('That word is not in the list')
            
    print('Goodbye')
    
