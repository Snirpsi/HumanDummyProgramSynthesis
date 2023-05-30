#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or iterates over a list of words. """    
    words = ['cat', 'dog', 'bird', 'birds', 'birds', 'cats', 'dogs', 'cats', 'dogs']
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word in words:
            print(word)
        else:
            print('That word is not in the list')
            
