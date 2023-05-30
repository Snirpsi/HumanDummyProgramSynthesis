#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    
    numbers = []
    
    while True:
        number = int(input('Enter a number: '))
        numbers.append(number)
        
        if number == 0: break
    
    print('The numbers are: ')
    
    for number in numbers:
        print(number)
    
    print('\nThe sum of the numbers is ', sum(numbers))
    
    print('The average of the numbers is ', sum(numbers) / len(numbers))
    
    print('The sum of the squares of the numbers is ', sum(numbers) ** 2)
    
    print('The average of the squares of the numbers is ', sum(numbers) ** 0.5