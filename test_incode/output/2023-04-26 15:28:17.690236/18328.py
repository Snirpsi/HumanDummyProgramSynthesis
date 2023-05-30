#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words or stores fruits. """    
    
    words = read_words()
    
    fruit = calculate_fruit(words)
    
    write_words(fruit)
    
