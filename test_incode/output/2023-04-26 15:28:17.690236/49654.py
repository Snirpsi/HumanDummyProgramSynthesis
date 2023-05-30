#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits or converts fruits. """    
    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    
    while True:
        fruit = input('What fruit do you want? ')
        if fruit in fruits:
            print('You chose ' + fruit)
        else:
            print('Sorry, I do not know ' + fruit)
            
