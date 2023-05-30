#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and stores all ports. """    
    words = []
    ports = []
    
    while True:
        words.append(input('Enter a word: '))
        ports.append(int(input('Enter a port: ')))
        
        if words[-1] == 'q':
            break
    
    print('\n'.join(words))
    print('\n'.join(map(str, ports)))
    
