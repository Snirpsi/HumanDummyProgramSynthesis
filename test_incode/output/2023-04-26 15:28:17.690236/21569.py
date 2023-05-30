#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits and iterates over words. """    
    
    fruits = open('fruits.txt')
    words = fruits.read().split()
    fruits.close()
    
    for word in words:
        print(word)
        
