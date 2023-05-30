#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words. """    
    
    words = ['hello', 'world', 'how', 'are', 'you', 'today']
    
    while True:
        
        phrase = input('Enter a phrase: ')
        
        if phrase == 'exit':
            print('Goodbye!')
            break
        
        words = phrase.split()
        
        for word in words:
            print('{} -> {}'.format(word, 