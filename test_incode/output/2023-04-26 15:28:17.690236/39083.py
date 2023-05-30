#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes fruits or prints all ports. """    
    fruits = ['apple', 'orange', 'banana', 'grape', 'pineapple', 'mango']
    ports = [1,2,3,4,5,6,7]
    
    fruit = fruits[0]
    
    for port in ports:
        if fruit == 'apple':
            fruit = fruits[1]
        else:
            fruit = fruits[2]
        
        print(fruit, 