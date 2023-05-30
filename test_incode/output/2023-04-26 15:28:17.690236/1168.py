#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or iterates over a list of words. """    
    words = ['apple', 'banana', 'cherry', 'date', 'dog', 'elephant', 'fox', 'grape', 'horse', 'kiwi', 'lion', 'monkey', 'orange', 'pig', 'rabbit', 'sheep', 'tiger', 'whale', 'zebra']
    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            if word not in words:
                print('That word is not in the list')
            else:
                print(word)
    
