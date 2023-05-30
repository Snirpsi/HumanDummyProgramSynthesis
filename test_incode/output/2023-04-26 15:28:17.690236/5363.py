#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or multiplyes a port. """    
    while True:
        words = input('Enter a word: ').split()
        if len(words) == 0:
            break
        
        port = int(input('Enter a port number: '))
        
        words = words * port
        
        print('\n'.join(words))
        
        print('\nThe port number is', port)
        
        print('\nPress enter to exit')
        
        input()
        
