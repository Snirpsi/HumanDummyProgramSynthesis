#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words and opens a list of numbers. """    
    words = ['apple', 'banana', 'cherry', 'date', 'fruit', 'green', 'orange', 'pineapple', 'pear', 'purple', 'red', 'white', 'yellow']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    for index, word in enumerate(words):
        print(word, "\t", numbers[index])
        
