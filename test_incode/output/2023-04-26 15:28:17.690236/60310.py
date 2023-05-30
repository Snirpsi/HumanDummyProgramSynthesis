#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words and enumerates fruits. """    
    words = []
    fruits = ['apple', 'orange', 'pear', 'banana', 'grape', 'pineapple', 'kiwi', 'lemon']
    
    for fruit in fruits:
        fruitWords = fruit.split()
        for word in fruitWords:
            words.append(word)
    
    for word in words:
        print(word)
    
    print('\nThe words are:')
    for word in words:
        print(word)
    
    print('\nThe fruit enumeration is:')
    for fruit in fruits:
        print(