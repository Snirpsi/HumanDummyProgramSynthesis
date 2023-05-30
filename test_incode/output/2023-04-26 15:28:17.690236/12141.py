#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input and multiplyes a list of words. """    
    
    words = ['hello', 'world', 'python', 'is', 'cool', 'to', 'play', 'with', 'me']
    
    while True:
        
        answer = input('Enter a word: ')
        
        if answer == 'quit':
            break
        
        answer = answer.lower()
        
        if answer not in words:
            print('That word is not in the list')
            continue
        
        print('The word is', answer)
        
        answer = answer * 