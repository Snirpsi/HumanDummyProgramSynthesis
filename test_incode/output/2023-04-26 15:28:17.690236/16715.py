#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and multiplyes fruits. """    
    
    numbers = []
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    
    for fruit in fruits:
        numbers.append(fruit)
        
    numbers_string = '\n'.join(numbers)
    
    print(numbers_string)
    
