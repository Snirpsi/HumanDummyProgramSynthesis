#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of words and calculates numbers. """    
    words = open("words.txt", "r").read().splitlines()
    numbers = []
    for word in words:
        numbers.append(word.count(","))
    numbers.sort()
    print(numbers)
    
