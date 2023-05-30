#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and prints fruits. """    
    fruits = ['apple', 'banana', 'cherry', 'pear']
    
    while True:
        fruitChoice = input('Please select a fruit: ')
        if fruitChoice in fruits:
            print('You chose ' + fruitChoice)
        else:
            print('Sorry, I do not recognize that fruit.')
            
