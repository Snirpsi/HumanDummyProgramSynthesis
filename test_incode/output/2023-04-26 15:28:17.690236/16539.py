#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers and stores user input. """    
    
    while True:
        numbers = []
        
        while True:
            number = input('Enter a number: ')
            numbers.append(number)
            
            if number == 'done':
                break
            
        print('The numbers are:')
        
        for number in numbers:
            print(number)
            
        print('The sum of the numbers is {}'.format(sum(numbers)))
        
        print('Do you want to add more numbers?')
        
        answer = input('(y/n): ')
        
        if answer == 'y':
            print('Adding more numbers...')
            
            numbers.append(input('Enter a number: ')) 
            
            print('The numbers are:')
            
            for number in numbers:
                print(number)
            
            print('The sum of the numbers is {}'.format(sum(numbers)))
            
            print('Do you want to add more numbers?')
            
            answer = input('(y/n): ')
            
            if answer == 'y':
                print('Adding more numbers...')
                
                numbers.append(input('Enter a number: ')) 
                
                print('The numbers are:')
                
                for number in numbers:
                    print(number)
                
                print('The sum of the numbers is {}'.format(sum(numbers)))
                
                print('Do you want to add more numbers?')
                
                answer = input('(y/n): ')
                
                if answer == 'y':
                    print('Adding more numbers...')
                    
                    numbers.append(input('Enter a number: ')) 
                    
                    print('The numbers are:')
                    
                    for number in numbers:
                        print(number)
                    
                    print('The sum of the numbers is {}'.format(sum(numbers)))
                    
                    print('Do you want to add more numbers?')
                    
                    answer = input('(y/n): ')
                    
                    if answer == 'y':
                        break
                    
