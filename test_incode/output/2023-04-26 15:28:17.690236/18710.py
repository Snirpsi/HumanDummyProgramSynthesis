#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['a', 'b', 'c']
    
    while True:
        word = input('Enter a word: ')
        if word in words:
            words.remove(word)
        else:
            print('No such word')
            break
        
    print('Your word list is', words)
    
