#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or stores all ports. """    
    while True:
        words = []
        ports = []
        
        while True:
            word = input('Enter a word: ')
            if word == 'quit':
                break
            words.append(word)
            
        while True:
            port = input('Enter a port: '