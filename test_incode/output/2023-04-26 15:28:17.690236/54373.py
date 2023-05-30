#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    while True:
        
        print('The numbers are:')
        
        for number in numbers:
            print(number)
            
        print('')
        
        number = input('Enter a number: ')
        
        if number == 'q':
            break
        
        numbers.append(number)
        
        print('The numbers are:')
        
        for number in numbers:
            print(number)
            
        print('')
        
    print('Thank you for using my 