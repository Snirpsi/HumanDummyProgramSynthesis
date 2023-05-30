#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words and prints a port. """    
    words = ['word1', 'word2']
    port = '1234'
    
    while True:
        words = words + ['word3', 'word4']
        port = port + str(random.randint(1, 10000))
        
        print('Port:', port)
        
        print('Words:', words)
        
        print('