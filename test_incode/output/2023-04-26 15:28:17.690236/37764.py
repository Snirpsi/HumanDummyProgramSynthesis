#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers and opens fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        print('The list of fruits is: ', fruits)
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            print('You chose ' + fruit)
        else:
            print('Sorry, I did not pick ' + fruit)
