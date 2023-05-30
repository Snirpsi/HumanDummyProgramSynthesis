#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    while True:
        fruits.append(input('Enter a fruit: '))
        print(fruits)
        
