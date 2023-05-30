#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits and iterates over a list of words. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    words = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        for fruit in fruits:
            for word in words:
                if fruit != word:
                    break
            else:
                print(