#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits and enumerates user input. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'mango', 'kiwi']
    fruits_length = len(fruits)
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            fruits.append(fruit)
            
    print('Your fruit is', fruits[fruits_length-1])
    
