#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and adds fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit not in fruits:
            print('That fruit does not exist')
        else:
            print('The fruit is', fruit)
            fruits.append(fruit)
        
        print('The fruit list is now', fruits)
        
        print('Press enter to exit')
        input()
        
