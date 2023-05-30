#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits and adds a list of words. """    
    
    fruit = input("Enter a fruit: ")
    fruit = fruit.lower()
    fruit = fruit.strip()
    
    words = input("Enter a word: ")
    words = words.split()
    
    fruit = fruit.replace("