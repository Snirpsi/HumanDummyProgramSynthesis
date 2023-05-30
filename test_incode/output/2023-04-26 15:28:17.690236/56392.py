#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    fruits_iter = enumerate(fruits)
    while True:
        fruit, number = fruits_iter.next()
        print('You chose ' + fruit)
        if fruit == 'cherry':
            break
        else:
            print('You chose ' + fruit)
            print('You chose ' + str(number))
