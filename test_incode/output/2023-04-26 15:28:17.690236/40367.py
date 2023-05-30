#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word == '':
            print('You did not enter a word.')
        else:
            print('You entered a word:', word)
            
            print('Removing word:', word)
            
            remove