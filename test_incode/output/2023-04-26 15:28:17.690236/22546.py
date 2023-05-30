#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers and returns words. """    
    
    numbers = []
    
    while True:
        numbers.append(int(input('Enter a number: ')))
        
        if numbers[-1] == 0: break
        
    print('The numbers are:')
    
    for number in numbers:
        print(number)
        
    print('The words are:')
    
    for number in numbers:
        if number > 0:
            print(number, 'is', numbers[number - 1], '