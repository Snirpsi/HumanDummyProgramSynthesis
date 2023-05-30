#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and stores a port. """    
    
    words = []
    
    for word in open('words.txt'):
        words.append(word.rstrip())
    
    port = 0
    
    for word in words:
        
        port += 1
        
        print('{}: {}'.format(word, port))
    
    print('\nDone.')
    
