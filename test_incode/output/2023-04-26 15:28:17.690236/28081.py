#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = None
        while fruit not in fruits:
            fruit = input('Please select a fruit: ')
            if fruit == 'quit':
                break
            fruits.remove(fruit)
        print('You chose', fruit, '