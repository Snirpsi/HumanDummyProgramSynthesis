#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and multiplyes fruits. """    
    
    fruits = ['apple', 'orange', 'pear', 'banana', 'cherry']
    
    while True:
        word = ''
        
        while word not in fruits:
            word = input('Enter a word: ')
            
        if word in fruits:
            print('The word "' + word + '" is ' + fruits[word] + '