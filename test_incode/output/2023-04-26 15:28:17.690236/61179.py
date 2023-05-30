#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or opens user input. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        
        if word in ['quit', 'exit', 'quit']:
            break
        
        print('The word is', word)
        
    print('Goodbye!')
    
