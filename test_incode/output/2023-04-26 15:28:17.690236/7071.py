#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and iterates over numbers. """    
    
    fruits = ['apple', 'orange', 'banana', 'pear', 'grape', 'pineapple', 'peach', 'mango']
    
    fruits_iter = iter(fruits)
    
    while True:
        try:
            fruit = next(fruits_iter)
            
            print('{} is {}'.format(fruit, next(fruits_iter)))
            
        except StopIteration:
            break
    
    print('Done')
    
