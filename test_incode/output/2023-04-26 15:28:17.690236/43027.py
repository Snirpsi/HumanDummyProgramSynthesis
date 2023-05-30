#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers or removes a list of numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Invalid input. Try again.')
        else:
            break
    
    numbers = []
    while number > 0:
        numbers.append(number)
        number -= 1
    
    print('The numbers are:')
    for number in numbers:
        print(number)
    
    removed = []
    while number > 0:
        removed.append(number)
        number -= 1
    
    print('The numbers are removed:')
    for number in removed:
        print(number)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
