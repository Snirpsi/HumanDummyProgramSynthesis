#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers and opens a list of words. """    
    numbers = open('numbers.txt')
    words = open('words.txt')
    
    numbers_words = []
    
    for line in numbers:
        numbers_words.append(line.strip())
    
    for line in words:
        numbers_words.append(line.strip())
    
    numbers_words.sort()
    
    for line in numbers_words:
        print(line)
    
    numbers.close()
    words.close()
    
