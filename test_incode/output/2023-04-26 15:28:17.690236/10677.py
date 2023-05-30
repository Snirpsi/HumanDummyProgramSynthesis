#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words and opens a list of numbers. """    
    
    words = []
    numbers = []
    
    with open('words.txt') as words:
        for line in words:
            words.append(line.strip())
    
    with open('numbers.txt') as numbers:
        for line in numbers:
            numbers.append(line.strip())
    
    words.sort()
    numbers.sort()
    
    for word in words:
        print(word)
    
    for number in numbers:
        print(number)
    
