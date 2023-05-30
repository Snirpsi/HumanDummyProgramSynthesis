#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or stores a list of numbers. """    
    
    numbers = []
    
    while True:
        number = input('Enter a number: ')
        
        if number == 'q':
            break
        
        numbers.append(int(number))
    
    print('The numbers are:')
    
    for number in numbers:
        print(number)
    
    print('The sum of the numbers is %d' % sum(numbers))
    
    print('The average of the numbers is %.1f' % sum(numbers) / len(numbers))
    
    print('The maximum value of the numbers is %d' % max(numbers))
    
    print('The minimum value of the numbers is %d' % min(numbers))
    
    print('The average of the numbers is %.2f' % sum(numbers) / len(numbers))
    
    print('The standard deviation of the numbers is %.2f' % 
          math.sqrt((sum(numbers)-sum(numbers)