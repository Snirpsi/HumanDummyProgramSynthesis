#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or stores a list of numbers. """    
    while True:
        word = input('Enter a word: ')
        number = int(input('Enter a number: '))
        words.append(word)
        numbers.append(number)
        if word == 'quit':
            break
        
    print('The word list is', words)
    print('The numbers list is', numbers)
    
