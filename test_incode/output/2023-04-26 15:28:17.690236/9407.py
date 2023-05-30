#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or returns numbers. """    
    while True:
        word = input('Enter a word: ')
        number = int(input('Enter a number: '))
        
        if word == 'quit':
            break
        
        if word == 'multiply':
            print(number * number)
        
        if word == 'exit':
            break
        
        if word == 'quit':
            break
        
        print('Invalid input')
        
