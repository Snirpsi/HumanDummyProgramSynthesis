#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers and iterates over a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    for index, word in enumerate(words):
        print(index, word)
        for number in numbers:
            print(index, number, words[number])
            
