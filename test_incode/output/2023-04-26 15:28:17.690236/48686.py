#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or calculates fruits. """    
    
    numbers = input('Enter numbers: ')
    fruits = input('Enter fruits: ')
    
    while True:
        numbers = numbers.split()
        fruits = fruits.split()
        
        if len(numbers) == 0 or len(fruits) == 0:
            print('Invalid input')
            continue
        
        if numbers[0] == 'quit':
            print('Goodbye')
            break
        
        if numbers[0] == 'add':
            numbers = numbers[1:]
            fruits = fruits[1:]
            
            if len(numbers) == 0 or len(fruits) == 0:
                print('Invalid input')
                continue
            
            numbers = map(int, numbers)
            fruits = map(int,fruits)
            
            numbers = sum(numbers)
            fruits = sum(fruits)
            
            print('The sum of your numbers is {}'.format(numbers))
            print('The sum of your fruits is {}'.format(fruits))
        
        if numbers[0] == 'subtract':
            numbers = numbers[1:]
            fruits = fruits[1:]
            
            if len(numbers) == 0 or len(fruits) == 0:
                print('Invalid input')
                continue
            
            numbers = map(int, numbers)
            fruits = map(int,fruits)
            
            numbers = sum(numbers)
            fruits = sum(fruits)
            
            print('The difference of your numbers is {}'.format(numbers))
            print('The difference of your fruits is {}'.format(fruits))
        
        if numbers[0] == 'multiply':
            numbers = numbers[1:]
            fruits = fruits[1:]
            
            if len(numbers) == 0 or len(fruits) == 0:
                print('Invalid input')
                continue
            
            numbers = map(int, numbers)
            fruits = map(int,fruits)
            
            numbers = sum(numbers)
            fruits = sum(fruits)
            
            print('The product of your numbers is {}'.format(numbers))
            print('The product of your fruits is {}'.format(fruits))
        
        if numbers[0] == 'divide':
            numbers = numbers[1:]
            fruits = fruits[1:]
            
            if len(numbers) == 0 or len(fruits) == 0:
                print('Invalid input')
                continue
            
            numbers = map(int, numbers)
            fruits = map(int,fruits)
            
            numbers = sum(numbers)
            fruits = sum(fruits)
            
            print('The quotient of your numbers is {}'.format(numbers))
            print('The quotient of your fruits is {}'.format(fruits))
        
        if numbers[0] == 'quit':
            print('Goodbye')
            break
        
        if numbers[0] == 'quit':
            print('Goodbye')
            break
