#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits or multiplyes words. """    
    fruit = input('Enter a fruit: ')
    word = input('Enter a word: ')
    
    if fruit == 'apple':
        print('The fruit ' + fruit + ' is ' + word + '!')
    elif fruit == 'banana':
        print('The fruit ' + fruit + ' is ' + word * 2 + '!')
    else:
        print('The fruit ' + fruit + ' is not an apple!')
    
