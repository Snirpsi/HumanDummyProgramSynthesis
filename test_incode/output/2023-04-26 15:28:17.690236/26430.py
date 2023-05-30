#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers. """    
    while True:
        number = int(input('Enter a number: '))
        numbers.append(number)
        
        if number == numbers[-1]:
            break
        
    print('The numbers are:')
    for number in numbers:
        print(number)
    
    print('The last number is', numbers[-1])
    
    print('The first number is', numbers[0])
    
    print('The last number is', numbers[-2])
    
    print('The first number is', numbers[