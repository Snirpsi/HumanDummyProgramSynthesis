#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or enumerates a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
    else:
        numbers = range(10)
    
    for number in numbers:
        print(number)
    
    print('\n')
    
    print('enumerate')
    
    for number, name in enumerate(numbers):
        print('{}: {}'.format(number, name))
    
    print('\n')
    
    print('range')
    
    for number in range(10):
        print('{}: {}'.format(number, number))
    
    print('\n')
    
    print('zip')
    
    for number, name in zip(numbers, names):
        print('{}: {}'.format(number, name))
    
    print('\n')
    
    print('map')
    
    for number, name in map(int, numbers):
        print('{}: {}'.format(number, name))
    
    print('\n')
    
    print('filter')
    
    for number, name in filter(lambda x: x % 2 == 0, numbers):
        print('{}: {}'.format(number, name))
    
    print('\n')
    
    print('reduce')
    
    numbers = range(10)
    
    numbers = numbers.reduce((lambda x, y: x + y), 0)
    
    print('{}: {}'.format(numbers, numbers))
    
    print('\n')
    
    print('reduce')
    
    numbers = range(10)
    
    numbers = numbers.reduce((lambda x, y: x + y), 0)
    
    print('{}: {}'.format(numbers, numbers))
    
    print('\n')
    
    print('reduce')
    
    numbers = range(10)
    
    numbers = numbers.reduce((lambda x, y: x + y), 0)
    
    print('{}: {}'.format(numbers, numbers))
    
    print('\n')
    
    print('reduce')
    
    numbers = range(10)
    
    numbers = numbers.reduce((lambda x, y: x + y), 0)
    
    print('{}: {}'.format(numbers, numbers))
    
    print('\n')
    
    print('reduce')
    
    numbers = range(10)
    
    numbers = numbers.reduce((lambda x, y: x + y), 0)
    
    print('{}: {}'.format(numbers, numbers))
    
    print('\n')
    
    print('reduce')
    
    numbers = range(10)
    
    numbers = numbers.reduce((lambda x, y: x + y), 0)
    
    print('{}: {}'.format(numbers, numbers))
    
    print('\n')
    
    print('reduce')
    
    numbers = range(10)
    
    numbers = numbers.reduce((lambda x, y: x + y), 0)
    
    print('{}: {}'.format(numbers, numbers))
    
    print('\n')
    
    print('reduce')
    
    numbers = range(10)
    
    numbers = numbers.reduce((lambda x, y: x + y), 