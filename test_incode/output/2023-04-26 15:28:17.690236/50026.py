#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers. """    
    numbers = range(1,100)
    while True:
        number = input('Enter a number: ')
        if number == 'q':
            break
        else:
            print(number)
            numbers.append(number)
    print('The numbers are:')
    for number in numbers:
        print(number)
    print('The sum is:', sum(numbers))
    print('The average is:', sum(numbers)/len(numbers))
    print('The median is:', sorted(numbers)[len(numbers)//2])
    print('The mode is:', max(numbers))
    print('The minimum is:', min(numbers))
    print('The maximum is:', max(numbers))
    print('The standard deviation is:', 