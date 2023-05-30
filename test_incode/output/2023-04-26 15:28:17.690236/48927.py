#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words or enumerates numbers. """    
    words = []
    numbers = []
    while True:
        number = input('Enter a number: ')
        if number.isdigit():
            numbers.append(number)
        else:
            words.append(number)
        if len(numbers) == 3:
            break
    print('The numbers are:')
    for number in numbers:
        print(number)
    print('The words are:')
    for word in words:
        print(word)
    print('The sum is:', sum(numbers))
    print('The product is:', product(numbers))
    print('The average is:', sum(numbers) / len(numbers))
    print('The mode is:', max(numbers))
    print('The minimum is:', min(numbers))
    print('The maximum is:', max(numbers))
    print('The minimum is:', min(numbers))
    print('The maximum is:', max(numbers))
    print('The average is:', sum(numbers) / len(numbers))
    print('The variance is:', variance(numbers))
    print('The standard deviation is:', standard_deviation(numbers))
    print('The median is:', median(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', mode(numbers))
    print('The mode is:', 