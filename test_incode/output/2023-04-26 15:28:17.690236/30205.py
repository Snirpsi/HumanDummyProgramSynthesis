#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input and adds a list of numbers. """    
    
    numbers = []
    
    while True:
        number = int(input('Enter a number: '))
        numbers.append(number)
        
        if number == -1:
            break
    
    print('The numbers entered were:')
    for number in numbers:
        print(number)
    
    print('The sum of the numbers is {}'.format(sum(numbers)))
    
    print('The average of the numbers is {}'.format(sum(numbers)/len(numbers)))
    
    print('The largest number entered is {}'.format(max(numbers)))
    
    print('The smallest number entered is {}'.format(min(numbers)))
    
    print('The average of the numbers is {}'.format(sum(numbers)/len(numbers)))
    
    print('The median of the numbers is {}'.format(sorted(numbers)[len(numbers)//2]))
    
    print('The median of the numbers is {}'.format(sorted(numbers)[len(numbers)//2] + sorted(numbers)[len(numbers)//2+1])/2)
    
    print('The median of the numbers is {}'.format(sorted(numbers)[len(numbers)//2] + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2)
    
    print('The median of the numbers is {}'.format(sorted(numbers)[len(numbers)//2] + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)[len(numbers)//2+1])/2 + sorted(numbers)