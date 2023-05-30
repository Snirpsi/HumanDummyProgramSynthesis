#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits and iterates over numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        print('Fruits:', fruits)
        print('Numbers:', numbers)
        
        fruit = input('Enter a fruit: ')
        number = int(input('Enter a number: '))
        
        if fruit == 'quit':
            break
        
        if number > len(numbers):
            print('Number too big')
            continue
        
        if fruit not in fruits:
            print('Fruit not in the list')
            continue
        
        print('You entered', fruit, 'with number', number)
        
        if number == numbers[number]:
            print('You win!')
            break
        
        print('Number not equal')
        
        fruit = input('Enter a fruit: ')
        number = int(input('Enter a number: '))
        
        if fruit == 'quit':
            break
        
        if number > len(numbers):
            print('Number too big')
            continue
        
        if fruit not in fruits:
            print('Fruit not in the list')
            continue
        
        print('You entered', fruit, 'with number', number)
        
        if number == numbers[number]:
            print('You win!')
            break
        
        print('Number not equal')
        
        fruit = input('Enter a fruit: ')
        number = int(input('Enter a number: '))
        
        if fruit == 'quit':
            break
        
        if number > len(numbers):
            print('Number too big')
            continue
        
        if fruit not in fruits:
            print('Fruit not in the list')
            continue
        
        print('You entered', fruit, 'with number', number)
        
        if number == numbers[number]:
            print('You win!')
            break
        
        print('Number not equal')
        
        fruit = input('Enter a fruit: ')
        number = int(input('Enter a number: '))
        
        if fruit == 'quit':
            break
        
        if number > len(numbers):
            print('Number too big')
            continue
        
        if fruit not in fruits:
            print('Fruit not in the list')
            continue
        
        print('You entered', fruit, 'with number', number)
        
        if number == numbers[number]:
            print('You win!')
            break
        
        print('Number not equal')
        
        fruit = input('Enter a fruit: ')
        number = int(input('Enter a number: '))
        
        if fruit == 'quit':
            break
        
        if number > len(