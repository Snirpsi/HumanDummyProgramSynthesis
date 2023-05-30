#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words and iterates over a list of words. """    
    
    words = ['cat', 'dog', 'horse', 'monkey']
    
    for word in words:
        print(word)
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(word)
            
    print('Done.')
    
