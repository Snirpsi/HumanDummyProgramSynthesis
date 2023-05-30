#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers or iterates over a list of words. """    
    
    words = ['cat', 'dog', 'mouse']
    
    numbers = []
    
    while True:
        numbers.append(input('Enter a number: '))
        
        if numbers[-1] == 'stop':
            break
    
    print('The numbers are:')
    
    for number in numbers:
        print(number)
    
    print('The words 