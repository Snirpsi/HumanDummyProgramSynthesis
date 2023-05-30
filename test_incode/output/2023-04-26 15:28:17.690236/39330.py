#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and returns a list of numbers. """    
    
    words = []
    
    with open('words.txt') as f:
        for line in f:
            words.append(line.strip())
    
    numbers = []
    
    for word in words:
        numbers.append(int(word))
    
    print(numbers)
    
