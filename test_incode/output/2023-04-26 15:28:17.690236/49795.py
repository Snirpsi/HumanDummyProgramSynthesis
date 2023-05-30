#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers and opens fruits. """    
    fruits = []
    
    while True:
        fruits.append(input('Enter a fruit: '))
        
        if fruits[-1] == 'done':
            break
        
    print('The fruits are:')
    for fruit in fruits:
        print(fruit)
    
    print('Thank you for using my program!')
    
