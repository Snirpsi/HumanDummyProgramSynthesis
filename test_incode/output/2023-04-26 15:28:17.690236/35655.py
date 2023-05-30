#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words and opens fruits. """    
    
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'peach', 'pizza', 'watermelon']
    
    for word in words:
        
        fruits = open(word, 'r')
        
        for fruit in fruits:
            print(fru