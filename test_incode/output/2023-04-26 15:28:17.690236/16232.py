#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers. """    
    
    numbers = []
    
    while True:
        number = int(input('Enter a number: '))
        
        if number < 1:
            print('Invalid number')
            continue
        
        numbers.append(number)
        
        if number == len(numbers):
            print('Done')
            break
    
    print('The numbers are:')
    
    for number in numbers:
        print(number)
    
    print('The sum of the numbers is {}'.format(sum(numbers)))
    
