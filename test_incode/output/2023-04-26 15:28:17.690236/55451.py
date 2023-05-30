#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of words or converts a list of numbers. """    
    while True:
        words = input('Enter a word: ')
        numbers = input('Enter a number: ')
        
        if words == 'exit':
            break
        
        if words == 'add':
            words += numbers
            print(words)
        
        if words == 'convert':
            numbers = numbers.split()
            words = []
            for number in numbers:
                words.append(int(number))
            print(words)
        
        print('\n')
        
