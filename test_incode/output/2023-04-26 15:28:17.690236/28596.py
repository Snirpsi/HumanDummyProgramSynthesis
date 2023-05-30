#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers and multiplyes numbers. """    
    
    numbers = []
    
    while True:
        numbers.append(int(input('Enter a number: ')))
        
        if len(numbers) == 3:
            break
        
    numbers = list(map(lambda x: x * 2, numbers))
    
    print('The product of the three entered numbers is: ', numbers)
    
