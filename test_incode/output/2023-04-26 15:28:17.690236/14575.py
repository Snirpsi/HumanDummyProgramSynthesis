#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or iterates over a list of words. """    
    
    words = ['apple', 'banana', 'cherry']
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            break
        else:
            print(words[fruit])
            
