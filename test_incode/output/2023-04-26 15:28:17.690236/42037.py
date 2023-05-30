#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers and removes user input. """    
    
    numbers = []
    
    while True:
        number = int(input('Enter a number: '))
        numbers.append(number)
        
        if number == 0: break
    
    numbers = list(set(numbers))
    
    print('The numbers you entered are:')
    
    for number in numbers:
        print(number)
    
    numbers_removed = numbers[:]
    
    print('The numbers you entered before were 