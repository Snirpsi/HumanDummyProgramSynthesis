#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words and stores fruits. """    
    words = ['apple', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruits.append(input('Enter a fruit: '))
        
        if fruits[-1] == '':
            fruits.pop()
        
        words.append(input('Enter a word: '))
        
        if words[-1] == '':
            words.pop()
        
        print(' '.join(fruits))
        
        print(' '.join(words))
        
        print('')
        
        print('Press Enter to exit')
        
        input()
        
