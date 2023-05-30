#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or adds a port. """    
    while True:
        word = input('Enter a word: ')
        port = int(input('Enter a port number: '))
        
        if port > 0 and port < 65535:
            print('The word is', word, 'and the port is', port)
        else:
            print('The word is', word, 'and the port is', port, '