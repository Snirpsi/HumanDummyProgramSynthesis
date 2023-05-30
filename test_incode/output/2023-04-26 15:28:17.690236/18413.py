#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and removes fruits. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    numbers_without_fruits = [x for x in numbers if x not in ['apple', 'banana', 'cherry', 'pear']]
    
    print(numbers_without_fruits)
    
