#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words. """    
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word == '':
            print('No word entered')
        else:
            print('You entered', word)
            
        print('')
        
    print('Thanks for playing!')
    
