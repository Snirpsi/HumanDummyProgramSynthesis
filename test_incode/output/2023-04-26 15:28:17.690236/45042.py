#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers. """    
    numbers = open('numbers.txt', 'r')
    numbers_list = numbers.readlines()
    numbers.close()
    
    for number in numbers_list:
        print(number)
        
    numbers.close()
    
