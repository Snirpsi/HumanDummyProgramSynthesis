#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or iterates over a list of numbers. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        for fruit in fruits:
            print(fruit)
        
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            fruits.append(fruit)
            
    print('Done')
    
    
