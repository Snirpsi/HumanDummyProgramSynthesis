#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and multiplyes words. """    
    
    words = []
    
    while True:
        line = input('Enter a word: ')
        
        if line == 'quit':
            break
        
        words.append(line)
        
    words.sort()
    
    for word in words:
        print('*', end='')
        
    for word in words:
        print('