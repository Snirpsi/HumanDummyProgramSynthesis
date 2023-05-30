#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words and opens numbers. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'q':
            break
        
        words.append(word)
    
    numbers = []
    
    while True:
        number = input('Enter a number: ')
        
        if number == 'q':
            break
        
        numbers.append(number)
    
    numbers = numbers + words
    
    print('\n'.join(numbers))
    
