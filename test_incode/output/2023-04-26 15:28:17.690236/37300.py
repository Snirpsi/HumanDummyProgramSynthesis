#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers and stores fruits. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'grape', 'mango']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    while True:
        number = numbers.pop(0)
        fruit = fruits.pop(0)
        
        print('The number is', number, 'and the fruit is', fruit)
        
        if number > 8:
            break
        
    print('The end')
    
