#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or opens a port. """    
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            print('Goodbye!')
            break
        else:
            print('You said: %s' % word)
            
    