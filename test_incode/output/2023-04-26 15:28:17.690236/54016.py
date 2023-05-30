#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers or opens user input. """    
    
    numbers = []
    
    while True:
        number = int(input('Enter a number: '))
        numbers.append(number)
        
        if number == -1:
            break
    
    print('The numbers are: ')
    
    for number in numbers:
        print(number)
    
    print('Thank you for using my program!')
    
