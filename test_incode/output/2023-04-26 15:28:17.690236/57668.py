#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or converts a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'q':
            break
        
    words = list(set(words))
    
    for word in words:
        print(word)
        
