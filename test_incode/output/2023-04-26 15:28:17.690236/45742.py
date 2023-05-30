#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and returns fruits. """    
    words = ['apple', 'banana', 'orange', 'mango', 'grape', 'peach', 'pineapple', 'plum', 'strawberry', 'watermelon']
    fruits = []
    
    while True:
        fruits.append(random.choice(words))
        
        print('The fruit is: ', fruits[-1])
        
        print('Press enter to exit')
        
        try:
            