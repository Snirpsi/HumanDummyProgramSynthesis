#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and removes a port. """    
    words = []
    port = '8080'
    
    while True:
        words.append(input('Enter a word: '))
        
        if words[-1] == port:
            words.pop()
            
        print(' '.join(words))
        
        print('\nPress Enter to exit')
        
        input()
        
