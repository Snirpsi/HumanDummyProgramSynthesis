#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or adds numbers. """    
    words = ['cat', 'dog', 'mouse', 'horse', 'sheep']
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word in words:
            print(word + ' is a word!')
        else:
            print(word + ' is not a word!')
    
    print('Goodbye!')
    
