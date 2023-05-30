#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words. """    
    
    words = ['hello', 'world', 'python', 'is', 'it', 'fun']
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'exit':
            break
        
        if word in words:
            print(word + ' is 