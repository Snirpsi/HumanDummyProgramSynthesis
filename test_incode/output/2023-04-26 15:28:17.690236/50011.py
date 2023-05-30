#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and iterates over a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            print(word)
            for word in words:
                print(word)
            
