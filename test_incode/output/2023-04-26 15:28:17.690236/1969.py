#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits and prints user input. """    
    fruits = ['apple', 'banana', 'cherry']
    
    fruits_choice = input('What fruit do you want? ')
    
    if fruits_choice in fruits:
        print('You chose ' + fruits_choice + '!')
    else:
        print('You chose ' + fruits_choice + '! 