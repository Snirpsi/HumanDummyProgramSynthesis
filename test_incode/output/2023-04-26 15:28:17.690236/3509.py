#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and removes a list of numbers. """    
    words = []
    numbers = []
    while True:
        word = input('Enter a word: ')
        numbers.append(int(input('Enter a number: ')))
        words.append(word)
        
        if word == 'q':
            break
        
    print('\n'.join(words))
    print('\n'.join(numbers))
    
