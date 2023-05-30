#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and stores fruits. """    
    
    words = ['apple', 'banana', 'orange', 'kiwi', 'grape', 'watermelon', 'pineapple', 'lemon']
    fruits = []
    
    for word in words:
        fruits.append(word)
    
    print('The fruits are:')
    for fruit in fruits:
        print(fruit)
    
    
