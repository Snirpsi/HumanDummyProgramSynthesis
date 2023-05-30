#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    while True:
        fruits = input('Enter fruits: ')
        if fruits == 'quit':
            break
        fruits.remove('apple')
        fruits.remove('orange')
        fruits.remove('pear')
        fruits.remove('banana')
        print('Fruits: ' + ', '.join(