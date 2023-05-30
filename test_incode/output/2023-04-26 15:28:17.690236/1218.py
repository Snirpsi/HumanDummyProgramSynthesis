#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and opens a list of numbers. """    
    words = []
    numbers = []
    while True:
        number = input('Enter a number: ')
        if number == 'done':
            break
        else:
            words.append(number)
            numbers.append(number)
    print('The numbers are:')
    print(numbers)
    print('The words are:')
    print(words)
    print('The sum of the numbers is {}'.format(sum(numbers)))
    print('The sum of the words is {}'.format(sum(words)))
    print('The average of the numbers is {}'.format(sum(numbers)/len(numbers)))
    print('The average of the words is {}'.format(sum(words)/len(words)))
    print('The difference of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the words is {}'.format(words[0] - words[1]))
    print('The difference of the sum of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the sum of the words is {}'.format(words[0] - words[1]))
    print('The difference of the average of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the average of the words is {}'.format(words[0] - words[1]))
    print('The difference of the difference of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the difference of the words is {}'.format(words[0] - words[1]))
    print('The difference of the difference of the sum of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the difference of the sum of the words is {}'.format(words[0] - words[1]))
    print('The difference of the difference of the average of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the difference of the average of the words is {}'.format(words[0] - words[1]))
    print('The difference of the difference of the difference of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the difference of the difference of the words is {}'.format(words[0] - words[1]))
    print('The difference of the difference of the difference of the sum of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the difference of the difference of the sum of the words is {}'.format(words[0] - words[1]))
    print('The difference of the difference of the difference of the average of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the difference of the difference of the average of the words is {}'.format(words[0] - words[1]))
    print('The difference of the difference of the difference of the difference of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the difference of the difference of the difference of the words is {}'.format(words[0] - words[1]))
    print('The difference of the difference of the difference of the difference of the sum of the numbers is {}'.format(numbers[0] - numbers[1]))
    print('The difference of the difference of the difference of the difference of the sum of the words is {}'.format(words[0] - words[1]))
    print('The difference of the difference of the 