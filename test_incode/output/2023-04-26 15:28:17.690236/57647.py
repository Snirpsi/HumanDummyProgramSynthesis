#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or calculates fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'pear', 'grape', 'mango']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            print(fruit)
            
    print('The fruit ' + fruit + ' is ' + fruits[fruits.index(