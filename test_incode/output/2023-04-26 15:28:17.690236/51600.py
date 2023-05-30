#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words or converts a port. """    
    while True:
        word = input('Enter a word: ')
        port = int(input('Enter a port number: '))
        
        if word == 'quit':
            break
        
        if port == 9999:
            print('Bye!')
            break
        
        print('Converting %d to %s' % (port, word))
        
        