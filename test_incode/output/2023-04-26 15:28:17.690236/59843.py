#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and prints numbers. """    
    import sys
    words = []
    for word in sys.argv[1:]:
        words.append(word.strip())
    
    numbers = []
    for word in words:
        numbers.append(int(word))
    
    for number in numbers:
        print(number)
    
