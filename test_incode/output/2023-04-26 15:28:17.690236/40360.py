#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and calculates numbers. """    
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    numbers = []
    
    while True:
        
        number = input('Enter a number: ')
        
        if number == 'done':
            break
        
        number = int(number)
        
        if number > 0:
            numbers.append(number)
        
    print('The numbers are:')
    
    for number in numbers:
        print(number)
        
    print('The sum is:', sum(numbers))
    
    print('The average is:', sum(numbers) / len(numbers))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, 1))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, 0))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -1))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -2))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -3))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -4))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -5))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -6))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -7))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -8))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -9))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -10))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -11))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -12))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -13))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -14))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -15))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -16))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -17))
    
    print('The product is:', reduce(lambda x, y: x * y, numbers, -18))
    
    print('The product 