#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['apple', 'banana', 'cherry', 'date', 'dog', 'elephant', 'fox', 'horse', 'lion',
              'monkey', 'orange', 'pig', 'rabbit', 'sheep', 'tiger', 'whale', 'zebra']
    
    word = ''
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word in words:
            print(word)
        else:
            print('That word is not in the list')
            
    print('Done')
    
