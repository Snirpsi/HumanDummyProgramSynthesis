#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers. """    
    
    while True:
        number = int(input('Enter a number: '))
        
        if number == 0: break
        
        total = 0
        
        for digit in str(number):
            total += int(digit)
        
        print('The total is', total)
        
        print('Do you want to continue? (y/n)')
        
        answer = input('> ')
        
        if answer == 'y':
            print('Goodbye!')
            break
        
        if answer == 'n':
            print('Goodbye!')
            break
        
        print('Invalid input!')
        
    print('Bye!')
    
