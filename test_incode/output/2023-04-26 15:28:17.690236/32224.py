#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits or adds a list of words. """    
    
    words = ['apple', 'banana', 'cherry', 'date', 'dog', 'fruit', 'goat', 'horse', 'lion', 'monkey', 'orange', 'pig', 'sheep', 'tiger', 'tree', 'vegetable', 'water']
    
    while True:
        fruits = input('Enter a fruit: ')
        
        if fruits == 'quit':
            print('Goodbye')
            break
        
        if fruits not in words:
            print('Sorry, I don\'t know that fruit.')
        else:
            print('I like ' + fruits)
            
        print('')
    
