#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports and enumerates a list of words. """    
    while True:
        port = input('Enter a port number: ')
        words = []
        
        for word in port2words(port):
            words.append(word)
        
        print('\n'.join(words))
        
        print('\nPress enter to exit.')
        
        input()
        
