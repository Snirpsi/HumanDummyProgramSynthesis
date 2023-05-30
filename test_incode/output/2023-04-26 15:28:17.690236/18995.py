#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or stores numbers. """    
    
    while True:
        word = input('Enter a word: ')
        number = input('Enter a number: ')
        
        if word == 'exit':
            break
        
        if word == 'quit':
            break
        
        if number == 'exit':
            break
        
        if number == 'quit':
            break
        
        print('The word is', word)
        print('The number is', number)
        
        print('\n')
        
    print('Thank you for using the 