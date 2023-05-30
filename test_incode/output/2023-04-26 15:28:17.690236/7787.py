#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words and calculates numbers. """    
    words = []
    
    with open('words.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    
    words.sort()
    
    numbers = []
    
    for word in words:
        numbers.append(len(word))
    
    numbers.sort()
    
    print('\n'.join(map(str, numbers)))
    
