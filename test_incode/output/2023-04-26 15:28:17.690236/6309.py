#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and multiplyes fruits. """    
    
    wordlist = ["apple", "orange", "banana", "pear", "mango"]
    fruits = ["apple", "orange", "banana", "pear", "mango"]
    
    fruits_multiplied = []
    
    for fruit in fruits:
        fruits_multiplied.append(fruit*wordlist[wordlist.index(fruit)