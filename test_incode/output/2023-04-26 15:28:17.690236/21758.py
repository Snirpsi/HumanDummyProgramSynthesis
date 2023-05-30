#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits and opens a list of numbers. """    
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        fruits.append(input('Enter a fruit: '))
        numbers.append(int(input('Enter a number: ')))
        
        print('Your fruit is: ', fruits[-1])
        print('Your number is: ', numbers[-1])
        
        print('Do you want to add another fruit? y/n')
        
        choice = input('