#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port or calculates words. """    
    
    port = int(input('Enter a port number: '))
    words = input('Enter a word: ')
    
    if port < 0 or port > 65535:
        print('Invalid port number')
        
    elif len(words) < 2:
        print('Invalid word')
        
    else:
        print('The port number {} has {} word(s)'.format(port, len(words)))
        
