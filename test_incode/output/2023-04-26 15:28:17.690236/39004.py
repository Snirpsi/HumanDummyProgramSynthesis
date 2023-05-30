#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    while True:
        fruits.append(input('Enter a fruit: '))
        if fruits == ['apple', 'orange', 'banana', 'cherry']:
            break
        else:
            print('Sorry, I did not understand your input.')
    print('The fruit was:', fruits)
    
