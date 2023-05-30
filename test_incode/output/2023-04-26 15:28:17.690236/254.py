#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or multiplyes a list of words. """    
    while True:
        port = int(input('Enter a port number: '))
        if port < 1 or port > 65535:
            print('Invalid port number')
        else:
            print('The port number is:', port)
            break
        
    words = []
    while True:
        word = input('Enter a word: ')
        if word == '':
            print('