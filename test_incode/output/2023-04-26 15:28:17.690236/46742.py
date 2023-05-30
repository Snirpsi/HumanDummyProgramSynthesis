#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and prints fruits. """    
    
    import sys
    
    words = ['apple', 'banana', 'orange', 'pear', 'kiwi']
    
    fruits = []
    
    for word in words:
        if word in sys.argv:
            fruits.append(word)
    
    for fruit in fruits:
        print(fruit)
    
    print('Done')
    
