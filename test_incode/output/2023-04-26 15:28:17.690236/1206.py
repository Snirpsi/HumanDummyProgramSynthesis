#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers. """    
    
    numbers = []
    
    while True:
        number = int(input('Enter a number: '))
        
        if number in numbers:
            print('This number already exists.')
        else:
            numbers.append(number)
            
            print('Number added')
            
            print('The numbers are:')
            
            for number in numbers:
                print(number)
            
            print('\nPress enter to exit.')
            
            input()
            
            break
            
    print('\nGoodbye!')
    
