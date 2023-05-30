#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words and opens a port. """    
    while True:
        words = []
        port = 5000
        
        while True:
            word = input('Enter a word: ')
            if word == 'q':
                break
            words.append(word)
            
        while True:
            port = input('Enter a port number: ')
            if port == 'q':
                break
            port = int(port)
            
        words.sort()
        
        for word in words:
            