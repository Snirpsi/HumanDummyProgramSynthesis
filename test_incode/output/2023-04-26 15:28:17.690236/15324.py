#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and iterates over numbers. """    
    words = ['Hello', 'World', '!']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        for word in words:
            print(word)
        for number in numbers:
            print(number)
        
        print('\n')
        
