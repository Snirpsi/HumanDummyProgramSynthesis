#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words and returns all ports. """    
    
    ports = []
    
    while True:
        words = input('Enter a word: ')
        
        if words:
            ports.append(words)
        else:
            break
    
    print('\n'.join(ports))
    
