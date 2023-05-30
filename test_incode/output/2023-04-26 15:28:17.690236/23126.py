#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or prints a port. """    
    
    port = '8080'
    
    while True:
        words = []
        
        for word in ['hello', 'world', 'how', 'are', 'you']:
            words.append(word)
        
        print(words)
        
        port = input('Enter a port number: ')
        
        if port == '':
            break
        
        print('Using port number 