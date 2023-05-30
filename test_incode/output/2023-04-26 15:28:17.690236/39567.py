#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or returns fruits. """    
    
    words = ['apple', 'banana', 'orange', 'mango', 'pear', 'grape', 'pineapple', 'kiwi']
    
    fruits = []
    
    while True:
        fruits.append(random.choice(words))
        
        if fruits[-1] == 'apple':
            break
        
    print('The fruits are:')
    for fruit in fruits:
        print(fruit)
        
    print('\nThe fruit that ends up being apple is ' + fruits[-1])
    
    print('\nThe fruit that ends up being mango is ' + fruits[-2])
    
    print('\nThe fruit that ends up being pineapple is ' + fruits[-3])
    
    print('\nThe fruit that ends up being kiw