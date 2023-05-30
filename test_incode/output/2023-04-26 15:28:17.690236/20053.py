#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds fruits. """    
    
    fruits = ['apple', 'orange', 'pear', 'banana', 'watermelon']
    
    for fruit in fruits:
        print('Adding ' + fruit + ' to inventory.')
        
        inventory = input('Enter the fruit you want to add: ')
        
        if inventory not in fruits:
            print('Invalid input. Try again.')
            continue
        
        inventory.append(fruit)
        
        print('Inventory now contains: ' + ', '.join(inventory))
        
        print('Done.')
    
